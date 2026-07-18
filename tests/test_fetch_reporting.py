from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from io import StringIO
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock

import pytest
from rich.console import Console

from src.models import ContentItem, SourceType
from src.orchestrator import FetchReport, HorizonOrchestrator, SourceFetchOutcome


SINCE = datetime(2026, 1, 1, tzinfo=timezone.utc)


def make_item(item_id: str) -> ContentItem:
    return ContentItem(
        id=item_id,
        source_type=SourceType.RSS,
        title=item_id,
        url=f"https://example.com/{item_id}",
        content="content",
        author="tester",
        published_at=SINCE,
    )


def make_orchestrator() -> HorizonOrchestrator:
    orchestrator = object.__new__(HorizonOrchestrator)
    orchestrator.console = Console(file=StringIO())
    orchestrator.last_fetch_report = None
    return orchestrator


def make_sources(**overrides):  # type: ignore[no-untyped-def]
    values = {
        "github": [],
        "hackernews": SimpleNamespace(enabled=False),
        "rss": [],
        "reddit": SimpleNamespace(enabled=False),
        "telegram": SimpleNamespace(enabled=False),
        "twitter": None,
        "openbb": None,
        "ossinsight": SimpleNamespace(enabled=False),
        "gdelt": None,
        "google_news": None,
    }
    values.update(overrides)
    return SimpleNamespace(**values)


class StubScraper:
    def __init__(self, result=None, error: Exception | None = None):  # type: ignore[no-untyped-def]
        self.result = [] if result is None else result
        self.error = error

    async def fetch(self, since):  # type: ignore[no-untyped-def]
        if self.error:
            raise self.error
        return self.result


def test_all_success_empty_has_normal_success_report(monkeypatch) -> None:
    orchestrator = make_orchestrator()
    orchestrator.config = SimpleNamespace(  # type: ignore[assignment]
        sources=make_sources(github=[object()]), extractors={}
    )
    monkeypatch.setattr(
        "src.orchestrator.GitHubScraper",
        lambda config, client: StubScraper(),
    )

    items = asyncio.run(orchestrator.fetch_all_sources(SINCE))

    assert items == []
    assert orchestrator.last_fetch_report is not None
    assert orchestrator.last_fetch_report.status == "success"
    assert orchestrator.last_fetch_report.all_failed is False
    assert orchestrator.last_fetch_report.to_dict()["empty"] == 1


def test_partial_failure_keeps_items_and_source_names(monkeypatch) -> None:
    orchestrator = make_orchestrator()
    kept = make_item("kept")
    orchestrator.config = SimpleNamespace(  # type: ignore[assignment]
        sources=make_sources(
            github=[object()], hackernews=SimpleNamespace(enabled=True)
        ),
        extractors={},
    )
    monkeypatch.setattr(
        "src.orchestrator.GitHubScraper",
        lambda config, client: StubScraper([kept]),
    )
    monkeypatch.setattr(
        "src.orchestrator.HackerNewsScraper",
        lambda config, client: StubScraper(error=ValueError("unavailable")),
    )

    items = asyncio.run(orchestrator.fetch_all_sources(SINCE))

    assert items == [kept]
    assert orchestrator.last_fetch_report is not None
    report = orchestrator.last_fetch_report
    assert [outcome.source_name for outcome in report.outcomes] == ["GitHub", "Hacker News"]
    assert report.status == "partial_failure"
    assert report.failed_count == 1
    source_reports = report.to_dict()["sources"]
    assert isinstance(source_reports, list)
    assert source_reports[1]["error"] == "ValueError: unavailable"


def test_native_run_raises_when_every_attempted_source_failed(monkeypatch) -> None:
    orchestrator = make_orchestrator()
    orchestrator.config = SimpleNamespace(  # type: ignore[assignment]
        email=None,
        filtering=SimpleNamespace(time_window_hours=24),
    )
    orchestrator.email_manager = None
    send_failure = AsyncMock()
    orchestrator.webhook_notifier = SimpleNamespace(send_failure=send_failure)  # type: ignore[assignment]
    report = FetchReport(
        [
            SourceFetchOutcome("GitHub", "failure", error="RuntimeError: down"),
            SourceFetchOutcome("RSS Feeds", "failure", error="TimeoutError: slow"),
        ]
    )

    async def fetch_all_sources(since):  # type: ignore[no-untyped-def]
        orchestrator.last_fetch_report = report
        return []

    monkeypatch.setattr(orchestrator, "fetch_all_sources", fetch_all_sources)

    with pytest.raises(RuntimeError, match="All 2 attempted sources failed.*GitHub.*RSS Feeds"):
        asyncio.run(orchestrator.run())

    send_failure.assert_awaited_once()


def test_native_run_writes_empty_daily_outputs(monkeypatch, tmp_path) -> None:
    orchestrator = make_orchestrator()
    orchestrator.config = SimpleNamespace(  # type: ignore[assignment]
        email=None,
        ai=SimpleNamespace(languages=["zh"]),
        filtering=SimpleNamespace(
            time_window_hours=24,
            category_groups={},
            default_group="other",
        ),
    )
    orchestrator.email_manager = None
    orchestrator.webhook_notifier = None
    summary_path = tmp_path / "summary.md"
    obsidian_path = tmp_path / "每日信息日报" / "daily.md"
    orchestrator.storage = SimpleNamespace(  # type: ignore[assignment]
        save_daily_summary=Mock(return_value=summary_path),
        save_obsidian_daily_note=Mock(return_value=obsidian_path),
    )

    async def fetch_all_sources(since):  # type: ignore[no-untyped-def]
        orchestrator.last_fetch_report = FetchReport(
            [SourceFetchOutcome("RSS Feeds", "empty")]
        )
        return []

    monkeypatch.setattr(orchestrator, "fetch_all_sources", fetch_all_sources)
    monkeypatch.setenv(
        "HORIZON_OBSIDIAN_OUTPUT_DIR",
        str(tmp_path / "每日信息日报"),
    )
    monkeypatch.chdir(tmp_path)

    asyncio.run(orchestrator.run())

    orchestrator.storage.save_daily_summary.assert_called_once()
    obsidian_call = orchestrator.storage.save_obsidian_daily_note.call_args
    assert obsidian_call.args[0] == str(tmp_path / "每日信息日报")
    assert "status: no_significant_updates" in obsidian_call.args[2]
    assert list((tmp_path / "docs" / "_posts").glob("*-summary-zh.md"))


def test_native_run_retries_when_partial_failure_returns_no_items(monkeypatch) -> None:
    orchestrator = make_orchestrator()
    orchestrator.config = SimpleNamespace(  # type: ignore[assignment]
        email=None,
        filtering=SimpleNamespace(time_window_hours=24),
    )
    orchestrator.email_manager = None
    orchestrator.webhook_notifier = None
    orchestrator.storage = SimpleNamespace(  # type: ignore[assignment]
        save_daily_summary=Mock(),
        save_obsidian_daily_note=Mock(),
    )

    async def fetch_all_sources(since):  # type: ignore[no-untyped-def]
        orchestrator.last_fetch_report = FetchReport(
            [
                SourceFetchOutcome("RSS Feeds", "empty"),
                SourceFetchOutcome(
                    "Twitter",
                    "failure",
                    error="TimeoutError: slow",
                ),
            ]
        )
        return []

    monkeypatch.setattr(orchestrator, "fetch_all_sources", fetch_all_sources)

    with pytest.raises(
        RuntimeError,
        match="No content was fetched while 1/2 sources failed",
    ):
        asyncio.run(orchestrator.run())

    orchestrator.storage.save_daily_summary.assert_not_called()
    orchestrator.storage.save_obsidian_daily_note.assert_not_called()
