"""Daily summary generation — pure programmatic rendering."""

import html
import re
from typing import Dict, List, Optional
from urllib.parse import quote, urlsplit

from ..models import CategoryGroupConfig, ContentItem
from ..obsidian_profiles import get_obsidian_daily_profile


_CJK = r"[\u4e00-\u9fff\u3400-\u4dbf]"
_ASCII = r"[A-Za-z0-9]"
_MARKDOWN_SPECIAL = re.compile(r"([\\`*_{}\[\]()<>#!|])")
_MARKDOWN_BLOCK_START = re.compile(r"(?m)^( {0,3})(>|[-+] |\d+[.)] )")
_URL_SAFE_CHARS = ":/?#[]@!$&'*,;=~%+"


def _escape_markdown(value: object) -> str:
    """Render untrusted text literally while retaining its readable content."""
    escaped = html.escape(str(value), quote=True)
    escaped = _MARKDOWN_SPECIAL.sub(r"\\\1", escaped)
    return _MARKDOWN_BLOCK_START.sub(r"\1\\\2", escaped)


def _safe_url(value: object) -> Optional[str]:
    """Return an HTML/Markdown-safe HTTP(S) URL, or None for unsafe URLs."""
    raw = str(value).strip()
    if not raw or any(ord(char) < 32 or ord(char) == 127 for char in raw):
        return None
    try:
        parsed = urlsplit(raw)
        if parsed.scheme.lower() not in {"http", "https"} or not parsed.netloc:
            return None
        parsed.port
    except (TypeError, ValueError):
        return None
    encoded = quote(raw, safe=_URL_SAFE_CHARS)
    return html.escape(encoded, quote=True)


def _pangu(text: str) -> str:
    """Insert a space between CJK and ASCII letters/digits (Pangu spacing)."""
    text = re.sub(rf"({_CJK})({_ASCII})", r"\1 \2", text)
    text = re.sub(rf"({_ASCII})({_CJK})", r"\1 \2", text)
    return text


def _inline_markdown(value: object) -> str:
    """Escape untrusted text and collapse it to one Markdown-safe line."""
    return re.sub(r"\s+", " ", _escape_markdown(value)).strip()


LABELS = {
    "en": {
        "header": "Horizon Daily",
        "source": "Source",
        "background": "Background",
        "discussion": "Discussion",
        "references": "References",
        "tags": "Tags",
        "selected_items": "From {total} items, {selected} important content pieces were selected",
        "empty_analyzed": "Analyzed {total} items, but none met the importance threshold.",
        "empty_body": (
            "No significant developments today. This might indicate:\n"
            "- A quiet day in your tracked sources\n"
            "- The AI score threshold is too high\n"
            "- Your information sources need expansion\n\n"
            "Consider:\n"
            "1. Lowering the `ai_score_threshold` in config.json\n"
            "2. Adding more diverse information sources\n"
            "3. Checking if the AI model is working correctly\n"
        ),
    },
    "zh": {
        "header": "Horizon 每日速递",
        "source": "来源",
        "background": "背景",
        "discussion": "社区讨论",
        "references": "参考链接",
        "tags": "标签",
        "selected_items": "从 {total} 条内容中筛选出 {selected} 条重要资讯。",
        "empty_analyzed": "已分析 {total} 条内容，但没有达到重要性阈值的条目。",
        "empty_body": (
            "今日暂无重要动态，可能原因：\n"
            "- 今天关注的信息源较平静\n"
            "- AI 评分阈值设置过高\n"
            "- 信息源种类有待扩充\n\n"
            "建议：\n"
            "1. 在 config.json 中降低 `ai_score_threshold`\n"
            "2. 添加更多多样化的信息源\n"
            "3. 检查 AI 模型是否正常工作\n"
        ),
    },
}


class DailySummarizer:
    """Generates daily Markdown summaries from pre-analyzed content items."""

    def __init__(self):
        pass

    async def generate_summary(
        self,
        items: List[ContentItem],
        date: str,
        total_fetched: int,
        language: str = "en",
    ) -> str:
        """Generate daily summary in Markdown format.

        Items are rendered in score-descending order (already sorted by orchestrator).

        Args:
            items: High-scoring content items (already enriched)
            date: Date string (YYYY-MM-DD)
            total_fetched: Total number of items fetched before filtering
            language: Output language, either "en" or "zh"

        Returns:
            str: Markdown formatted summary
        """
        labels = LABELS.get(language, LABELS["en"])

        if not items:
            return self._generate_empty_summary(date, total_fetched, labels)

        header = (
            f"# {labels['header']} - {date}\n\n"
            f"> {labels['selected_items'].format(total=total_fetched, selected=len(items))}\n\n"
            "---\n\n"
        )

        # TOC
        toc_entries = []
        for i, item in enumerate(items):
            _t = item.metadata.get(f"title_{language}") or item.title
            t = _escape_markdown(_t)
            if language == "zh":
                t = _pangu(t)
            score = item.ai_score or "?"
            toc_entries.append(f"{i + 1}. [{t}](#item-{i + 1}) \u2b50\ufe0f {score}/10")
        toc = "\n".join(toc_entries) + "\n\n---\n\n"

        parts = [self._format_item(item, labels, language, i + 1) for i, item in enumerate(items)]

        return header + toc + "".join(parts)

    def generate_obsidian_note(
        self,
        items: List[ContentItem],
        date: str,
        total_fetched: int,
        category_groups: Dict[str, CategoryGroupConfig],
        default_group: str = "other",
        report_profile: str = "ai",
    ) -> str:
        """Generate a fixed-schema Chinese daily note for an Obsidian vault."""
        profile = get_obsidian_daily_profile(report_profile)
        grouped_items: Dict[str, List[ContentItem]] = {
            key: [] for key in category_groups
        }
        grouped_items.setdefault(default_group, [])

        category_to_group: Dict[str, str] = {}
        for group_key, group in category_groups.items():
            for category in group.categories:
                category_to_group.setdefault(category, group_key)

        for item in items:
            category = item.metadata.get("category")
            group_key = (
                category_to_group.get(category, default_group)
                if isinstance(category, str)
                else default_group
            )
            grouped_items[group_key].append(item)

        sections = [
            (key, group.name or key, grouped_items[key])
            for key, group in category_groups.items()
        ]
        if default_group not in category_groups:
            default_group_name = "其他" if default_group == "other" else default_group
            sections.append(
                (default_group, default_group_name, grouped_items[default_group])
            )

        status = "complete" if items else "no_significant_updates"
        lines = [
            "---",
            f"type: {profile['note_type']}",
            f"date: {date}",
            f"status: {status}",
            "source: Horizon",
            f"total_fetched: {total_fetched}",
            f"selected_count: {len(items)}",
            "tags:",
            *(f"  - {tag}" for tag in profile["tags"]),
            "---",
            "",
            f"# {date} {profile['note_suffix']}",
            "",
            "> [!summary] 今日概览",
            f"> 今日共采集 {total_fetched} 条{profile['summary_subject']}，筛选出 {len(items)} 条重点资讯。",
            "",
            f"- 日报索引：[[{profile['folder_name']}/00-日报索引|{profile['index_title']}]]",
            "- 知识库索引：[[Wiki/index|知识库索引]]",
            "",
            "## 分类概览",
            "",
            "| 分类 | 条目数 |",
            "|---|---:|",
        ]

        for _, name, group_items in sections:
            lines.append(f"| {_inline_markdown(name)} | {len(group_items)} |")

        for _, name, group_items in sections:
            lines.extend(["", f"## {_inline_markdown(name)}", ""])
            if not group_items:
                lines.append("本类今日无入选条目。")
                continue
            for item in group_items:
                lines.extend(self._format_obsidian_item(item))

        lines.extend(
            [
                "",
                "## 知识库处理",
                "",
                f"- [ ] {profile['knowledge_task']}",
                f"- [ ] {profile['verification_task']}",
                "",
                "## 运行说明",
                "",
                "- 本日报由 Horizon 自动生成，原始链接保留在每条资讯中。",
                "- 评分与摘要用于信息筛选，不代表事实已经完成独立验证。",
                "",
            ]
        )
        return "\n".join(lines)

    def _format_obsidian_item(self, item: ContentItem) -> List[str]:
        """Format one item with every field required by the Obsidian schema."""
        meta = item.metadata
        title = _pangu(_inline_markdown(meta.get("title_zh") or item.title))
        url = _safe_url(item.url)
        title_link = f"[{title}]({url})" if url else title

        summary = (
            meta.get("detailed_summary_zh")
            or meta.get("detailed_summary")
            or item.ai_summary
            or "暂无"
        )
        reason = item.ai_reason or "暂无"
        background = meta.get("background_zh") or meta.get("background") or "暂无"
        discussion = (
            meta.get("community_discussion_zh")
            or meta.get("community_discussion")
            or "暂无"
        )

        source_name = meta.get("feed_name") or item.author or "unknown"
        source_parts = [
            _inline_markdown(item.source_type.value),
            _inline_markdown(source_name),
        ]
        if item.published_at:
            source_parts.append(
                f"{item.published_at.month}月{item.published_at.day}日 "
                f"{item.published_at:%H:%M}"
            )
        source_line = " · ".join(source_parts)
        if url:
            source_line += f" · [原文]({url})"

        tags = (
            ", ".join(f"`#{_inline_markdown(tag)}`" for tag in item.ai_tags)
            if item.ai_tags
            else "暂无"
        )
        lines = [
            f"### {title_link}",
            "",
            f"- **评分**: {item.ai_score if item.ai_score is not None else '?'}/10",
            f"- **摘要**: {_pangu(_inline_markdown(summary))}",
            f"- **入选理由**: {_pangu(_inline_markdown(reason))}",
            f"- **来源**: {source_line}",
            f"- **背景**: {_pangu(_inline_markdown(background))}",
            f"- **社区讨论**: {_pangu(_inline_markdown(discussion))}",
        ]

        references = meta.get("sources") or []
        if references:
            lines.append("- **参考资料**:")
            for reference in references:
                reference_title = _inline_markdown(
                    reference.get("title") or "未命名来源"
                )
                reference_url = _safe_url(reference.get("url", ""))
                if reference_url:
                    lines.append(f"  - [{reference_title}]({reference_url})")
                else:
                    lines.append(f"  - {reference_title}")
        else:
            lines.append("- **参考资料**: 暂无")

        lines.extend([f"- **标签**: {tags}", ""])
        return lines

    def generate_webhook_overview(
        self,
        items: List[ContentItem],
        date: str,
        total_fetched: int,
        language: str = "en",
    ) -> str:
        """Generate a compact overview for multi-message webhook delivery."""
        labels = LABELS.get(language, LABELS["en"])
        if not items:
            return self._generate_empty_summary(date, total_fetched, labels)

        if language == "zh":
            header = (
                f"# {labels['header']} - {date}\n\n"
                f"> 从 {total_fetched} 条内容中筛选出 {len(items)} 条重要资讯。\n\n"
                "下面会按新闻逐条发送详情，你可以只看感兴趣的标题。\n\n"
            )
        else:
            header = (
                f"# {labels['header']} - {date}\n\n"
                f"> Selected {len(items)} important items from {total_fetched} fetched items.\n\n"
                "Details will be sent item by item so you can read only the topics you care about.\n\n"
            )

        entries = []
        for i, item in enumerate(items, start=1):
            title = _escape_markdown(item.metadata.get(f"title_{language}") or item.title)
            if language == "zh":
                title = _pangu(title)
            score = item.ai_score or "?"
            url = _safe_url(item.url)
            title_link = f"[{title}]({url})" if url else title
            entries.append(f"{i}. {title_link} \u2b50\ufe0f {score}/10")

        return header + "\n".join(entries)

    def generate_webhook_item(
        self,
        item: ContentItem,
        language: str,
        index: int,
        total: int,
    ) -> str:
        """Generate one item message for multi-message webhook delivery."""
        labels = LABELS.get(language, LABELS["en"])
        prefix = f"第 {index}/{total} 条\n\n" if language == "zh" else f"Item {index}/{total}\n\n"
        return prefix + self._format_item(item, labels, language, index).rstrip("-\n ")

    def _format_item(self, item: ContentItem, labels: dict, language: str, index: int) -> str:
        """Format a single ContentItem into Markdown."""
        _title = item.metadata.get(f"title_{language}") or item.title
        title = _escape_markdown(_title)
        raw_url = str(item.url)
        url = _safe_url(raw_url)
        score = item.ai_score or "?"
        meta = item.metadata

        summary = (
            meta.get(f"detailed_summary_{language}")
            or meta.get("detailed_summary")
            or item.ai_summary
            or ""
        )
        background = meta.get(f"background_{language}") or meta.get("background") or ""
        discussion = (
            meta.get(f"community_discussion_{language}")
            or meta.get("community_discussion")
            or ""
        )

        summary = _escape_markdown(summary)
        background = _escape_markdown(background)
        discussion = _escape_markdown(discussion)

        if language == "zh":
            title = _pangu(title)
            summary = _pangu(summary)
            background = _pangu(background)
            discussion = _pangu(discussion)

        # Source line with parts joined by " · ", link appended at end
        source_type = item.source_type.value
        source_parts = [_escape_markdown(source_type)]
        if meta.get("subreddit"):
            source_parts.append(_escape_markdown(f"r/{meta['subreddit']}"))
        if meta.get("feed_name"):
            source_parts.append(_escape_markdown(meta["feed_name"]))
        else:
            source_parts.append(_escape_markdown(item.author or "unknown"))
        if item.published_at:
            if language == "zh":
                source_parts.append(
                    f"{item.published_at.month}月{item.published_at.day}日 "
                    f"{item.published_at:%H:%M}"
                )
            else:
                day = item.published_at.strftime("%d").lstrip("0")
                source_parts.append(item.published_at.strftime(f"%b {day}, %H:%M"))
        source_line = " \u00b7 ".join(source_parts)  # ·

        discussion_url = meta.get("discussion_url")
        if discussion_url:
            safe_discussion_url = _safe_url(discussion_url)
            if safe_discussion_url and str(discussion_url) != raw_url:
                source_line += f' · [{labels["discussion"]}]({safe_discussion_url})'

        title_link = f"[{title}]({url})" if url else title

        lines = [
            f'<a id="item-{index}"></a>',
            f"## {title_link} \u2b50\ufe0f {score}/10",  # ⭐️
            "",
            summary,
            "",
            source_line,
        ]

        if background:
            lines.append("")
            lines.append(f"**{labels['background']}**: {background}")

        sources = meta.get("sources") or []
        if sources:
            reference_items = []
            for source in sources:
                reference_title = html.escape(str(source.get("title", "")), quote=True)
                reference_url = _safe_url(source.get("url", ""))
                if reference_url:
                    reference_items.append(f'<li><a href="{reference_url}">{reference_title}</a></li>\n')
                else:
                    reference_items.append(f"<li>{reference_title}</li>\n")
            items_html = "".join(reference_items)
            lines += [
                "",
                f'<details><summary>{labels["references"]}</summary>\n<ul>\n{items_html}\n</ul>\n</details>',
            ]

        if discussion:
            lines.append("")
            lines.append(f"**{labels['discussion']}**: {discussion}")

        if item.ai_tags:
            tags_str = ", ".join([f"`#{_escape_markdown(t)}`" for t in item.ai_tags])
            lines.append("")
            lines.append(f"**{labels['tags']}**: {tags_str}")

        lines.append("")
        lines.append("---")

        return "\n".join(lines) + "\n\n"

    def _generate_empty_summary(self, date: str, total_fetched: int, labels: dict) -> str:
        """Generate summary when no high-scoring items were found."""
        return (
            f"# {labels['header']} - {date}\n\n"
            f"> {labels['empty_analyzed'].format(total=total_fetched)}\n\n"
            + labels["empty_body"]
        )
