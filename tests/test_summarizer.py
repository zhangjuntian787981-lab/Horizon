"""Unit tests for daily summary rendering."""

import asyncio
from datetime import datetime, timezone

import pytest

from src.ai.summarizer import DailySummarizer
from src.models import CategoryGroupConfig, ContentItem, SourceType


def _run_async(coro):
    return asyncio.run(coro)


def _make_item(idx: int) -> ContentItem:
    item = ContentItem(
        id=f"rss:item-{idx}",
        source_type=SourceType.RSS,
        title=f"Important Item {idx}",
        url=f"https://example.com/items/{idx}",
        content="content",
        author="tester",
        published_at=datetime(2026, 4, 25, 8, 0, tzinfo=timezone.utc),
    )
    item.ai_score = 8.0
    item.ai_summary = f"Summary for item {idx}."
    item.ai_tags = ["AI", "News"]
    return item


def _category_groups():
    return {
        "official": CategoryGroupConfig(
            name="官方 AI 动态",
            limit=2,
            categories=["official-ai"],
        ),
        "research": CategoryGroupConfig(
            name="研究与前沿信号",
            limit=2,
            categories=["ai-research"],
        ),
        "practice": CategoryGroupConfig(
            name="实践案例",
            limit=3,
            categories=["ai-cases"],
        ),
        "open_source": CategoryGroupConfig(
            name="开源工具",
            limit=3,
            categories=["ai-open-source"],
        ),
    }


def test_generate_obsidian_note_uses_fixed_schema_and_category_sections():
    summarizer = DailySummarizer()
    item = _make_item(1)
    item.metadata["category"] = "ai-research"

    result = summarizer.generate_obsidian_note(
        [item],
        date="2026-07-19",
        total_fetched=10,
        category_groups=_category_groups(),
    )

    assert result.startswith("---\ntype: ai_daily_briefing\ndate: 2026-07-19")
    assert "status: complete" in result
    assert "selected_count: 1" in result
    assert "| 研究与前沿信号 | 1 |" in result
    assert "| 官方 AI 动态 | 0 |" in result
    for heading in (
        "## 官方 AI 动态",
        "## 研究与前沿信号",
        "## 实践案例",
        "## 开源工具",
        "## 其他",
        "## 知识库处理",
        "## 运行说明",
    ):
        assert heading in result
    assert "- **参考资料**: 暂无" in result
    assert "[[每日信息日报/00-日报索引|每日信息日报索引]]" in result
    assert "[[Wiki/index|知识库索引]]" in result


def test_generate_empty_obsidian_note_keeps_the_same_sections():
    summarizer = DailySummarizer()

    result = summarizer.generate_obsidian_note(
        [],
        date="2026-07-19",
        total_fetched=0,
        category_groups=_category_groups(),
    )

    assert "status: no_significant_updates" in result
    assert "selected_count: 0" in result
    assert result.count("本类今日无入选条目。") == 5
    assert "## 官方 AI 动态" in result
    assert "## 其他" in result


def test_generate_ecommerce_obsidian_note_uses_fixed_profile():
    summarizer = DailySummarizer()
    item = _make_item(1)
    item.metadata["category"] = "ecommerce-platform"
    groups = {
        "platform": CategoryGroupConfig(
            name="平台规则与行业动态",
            limit=2,
            categories=["ecommerce-platform"],
        ),
        "ai_tools": CategoryGroupConfig(
            name="AI 电商工具与自动化",
            limit=2,
            categories=["ai-commerce"],
        ),
    }

    result = summarizer.generate_obsidian_note(
        [item],
        date="2026-07-19",
        total_fetched=5,
        category_groups=groups,
        report_profile="ecommerce",
    )

    assert result.startswith("---\ntype: ecommerce_daily_briefing\ndate: 2026-07-19")
    assert "# 2026-07-19 电商运营日报" in result
    assert "今日共采集 5 条电商运营相关信息" in result
    assert "[[每日电商运营日报/00-日报索引|每日电商运营日报索引]]" in result
    assert "## 平台规则与行业动态" in result
    assert "## AI 电商工具与自动化" in result
    assert "- [ ] 对平台政策、数据指标和案例结论进行交叉验证" in result
    assert "  - 电商日报" in result
    assert "  - AI电商" in result


def test_generate_obsidian_note_rejects_unknown_profile():
    summarizer = DailySummarizer()

    with pytest.raises(ValueError, match="Unsupported Obsidian daily profile"):
        summarizer.generate_obsidian_note(
            [],
            date="2026-07-19",
            total_fetched=0,
            category_groups=_category_groups(),
            report_profile="unknown",
        )


def test_generate_obsidian_note_uses_configured_default_group_and_fallback_name():
    summarizer = DailySummarizer()
    item = _make_item(1)
    item.metadata["category"] = "unmapped"
    groups = {
        "official": CategoryGroupConfig(
            name=None,
            limit=1,
            categories=["official-ai"],
        )
    }

    result = summarizer.generate_obsidian_note(
        [item],
        date="2026-07-19",
        total_fetched=1,
        category_groups=groups,
        default_group="misc",
    )

    assert "## official" in result
    assert "## misc" in result
    assert "| misc | 1 |" in result


def test_generate_obsidian_note_flattens_multiline_item_fields():
    summarizer = DailySummarizer()
    item = _make_item(1)
    item.metadata.update(
        {
            "category": "ai-research",
            "detailed_summary_zh": "摘要第一行\n摘要第二行",
            "background_zh": "背景第一行\n背景第二行",
            "community_discussion_zh": "讨论第一行\n讨论第二行",
        }
    )
    item.ai_reason = "理由第一行\n理由第二行"

    result = summarizer.generate_obsidian_note(
        [item],
        date="2026-07-19",
        total_fetched=1,
        category_groups=_category_groups(),
    )

    assert "- **摘要**: 摘要第一行 摘要第二行" in result
    assert "- **入选理由**: 理由第一行 理由第二行" in result
    assert "- **背景**: 背景第一行 背景第二行" in result
    assert "- **社区讨论**: 讨论第一行 讨论第二行" in result


def test_generate_webhook_overview_lists_items_without_full_details():
    summarizer = DailySummarizer()
    items = [_make_item(1), _make_item(2)]

    result = summarizer.generate_webhook_overview(
        items,
        date="2026-04-25",
        total_fetched=10,
        language="en",
    )

    assert "Selected 2 important items from 10 fetched items" in result
    assert "1. [Important Item 1](https://example.com/items/1)" in result
    assert "2. [Important Item 2](https://example.com/items/2)" in result
    assert "Summary for item 1." not in result


def test_generate_webhook_item_renders_single_item_detail():
    summarizer = DailySummarizer()

    result = summarizer.generate_webhook_item(
        _make_item(1),
        language="en",
        index=1,
        total=2,
    )

    assert result.startswith("Item 1/2")
    assert "## [Important Item 1](https://example.com/items/1)" in result
    assert "Summary for item 1." in result
    assert "**Tags**: `#AI`, `#News`" in result


def test_generate_webhook_item_includes_discussion_link_when_distinct():
    summarizer = DailySummarizer()
    item = _make_item(1)
    item.metadata["discussion_url"] = "https://news.ycombinator.com/item?id=1"

    result = summarizer.generate_webhook_item(
        item,
        language="en",
        index=1,
        total=1,
    )

    assert "tester · Apr 25, 08:00 · [Discussion](https://news.ycombinator.com/item?id=1)" in result


def test_generate_webhook_item_omits_discussion_link_when_same_as_item_url():
    summarizer = DailySummarizer()
    item = _make_item(1)
    item.metadata["discussion_url"] = item.url

    result = summarizer.generate_webhook_item(
        item,
        language="en",
        index=1,
        total=1,
    )

    assert "[Discussion](https://example.com/items/1)" not in result


def test_generate_webhook_item_uses_localized_discussion_label():
    summarizer = DailySummarizer()
    item = _make_item(1)
    item.metadata["discussion_url"] = "https://www.reddit.com/r/python/comments/abc123/test/"

    result = summarizer.generate_webhook_item(
        item,
        language="zh",
        index=1,
        total=1,
    )

    assert "[社区讨论](https://www.reddit.com/r/python/comments/abc123/test/)" in result


def test_generate_summary_zh_uses_localized_selection_header_and_numeric_date():
    summarizer = DailySummarizer()
    item = _make_item(1)

    result = _run_async(
        summarizer.generate_summary(
            [item],
            date="2026-04-25",
            total_fetched=10,
            language="zh",
        )
    )

    assert "> 从 10 条内容中筛选出 1 条重要资讯。" in result
    assert "rss · tester · 4月25日 08:00" in result
    assert "From 10 items" not in result
    assert "Apr 25, 08:00" not in result


def test_generate_empty_summary_zh_uses_localized_analyzed_line():
    summarizer = DailySummarizer()

    result = _run_async(
        summarizer.generate_summary(
            [],
            date="2026-04-25",
            total_fetched=10,
            language="zh",
        )
    )

    assert "> 已分析 10 条内容，但没有达到重要性阈值的条目。" in result
    assert "Analyzed 10 items" not in result


def test_generate_summary_escapes_untrusted_text_in_all_output_contexts():
    summarizer = DailySummarizer()
    item = _make_item(1)
    item.title = '<script>alert("title")</script> [click](javascript:alert(1))'
    item.ai_summary = '<img src=x onerror="alert(1)"> **summary**'
    item.author = '<svg onload="alert(1)">'
    item.ai_tags = ['tag`](javascript:alert(1))']
    item.metadata.update(
        {
            "feed_name": '<b onclick="alert(1)">feed</b>',
            "background": '<iframe src="data:text/html,bad"></iframe>',
            "community_discussion": '[bad](data:text/html,bad)',
            "sources": [{"title": '<img src=x onerror="alert(1)">', "url": "https://example.com/ref"}],
        }
    )

    result = _run_async(summarizer.generate_summary([item], "2026-04-25", 1))

    assert "<script>" not in result
    assert "<img src=x" not in result
    assert "<iframe" not in result
    assert "<b onclick" not in result
    assert "](javascript:" not in result
    assert "](data:text/html" not in result
    assert "&lt;script&gt;" in result
    assert "&lt;img src=x onerror=&quot;alert(1)&quot;&gt;" in result


def test_generate_summary_rejects_unsafe_urls_and_quote_injection():
    summarizer = DailySummarizer()
    item = _make_item(1)
    item.metadata.update(
        {
            "discussion_url": 'javascript:alert("discussion")',
            "sources": [
                {"title": 'Quoted "><script>alert(1)</script>', "url": 'https://example.com/\" onmouseover=\"alert(1)'},
                {"title": "JavaScript", "url": "javascript:alert(1)"},
                {"title": "Data", "url": "data:text/html,<script>alert(1)</script>"},
            ],
        }
    )

    result = _run_async(summarizer.generate_summary([item], "2026-04-25", 1))

    assert 'href="https://example.com/%22%20onmouseover=%22alert%281%29"' in result
    assert '<li>JavaScript</li>' in result
    assert '<li>Data</li>' in result
    assert 'href="javascript:' not in result
    assert 'href="data:' not in result
    assert '<script>' not in result


def test_generate_summary_preserves_normal_http_links():
    summarizer = DailySummarizer()
    item = _make_item(1)
    item.metadata.update(
        {
            "discussion_url": "https://example.com/discuss?id=1#comments",
            "sources": [{"title": "Useful reference", "url": "https://docs.example.com/path?q=one&lang=en"}],
        }
    )

    result = _run_async(summarizer.generate_summary([item], "2026-04-25", 1))

    assert "[Important Item 1](https://example.com/items/1)" in result
    assert "[Discussion](https://example.com/discuss?id=1#comments)" in result
    assert 'href="https://docs.example.com/path?q=one&amp;lang=en"' in result
