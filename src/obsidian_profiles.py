"""Fixed output profiles for Obsidian daily knowledge bases."""


OBSIDIAN_DAILY_PROFILES = {
    "ai": {
        "note_type": "ai_daily_briefing",
        "index_type": "ai_daily_index",
        "note_suffix": "AI 信息日报",
        "folder_name": "每日信息日报",
        "index_title": "每日信息日报索引",
        "summary_subject": "信息",
        "tags": ["AI日报", "信息知识库"],
        "knowledge_task": "将值得长期跟踪的结论沉淀到 [[Wiki/index|知识库]]",
        "verification_task": "对社区观点或未验证信息进行交叉验证",
    },
    "ecommerce": {
        "note_type": "ecommerce_daily_briefing",
        "index_type": "ecommerce_daily_index",
        "note_suffix": "电商运营日报",
        "folder_name": "每日电商运营日报",
        "index_title": "每日电商运营日报索引",
        "summary_subject": "电商运营相关信息",
        "tags": ["电商日报", "AI电商", "信息知识库"],
        "knowledge_task": "将可复用的运营策略、案例和工具沉淀到 [[Wiki/index|知识库]]",
        "verification_task": "对平台政策、数据指标和案例结论进行交叉验证",
    },
}


def get_obsidian_daily_profile(profile_name: str) -> dict:
    """Return one supported Obsidian daily profile."""
    try:
        return OBSIDIAN_DAILY_PROFILES[profile_name]
    except KeyError as exc:
        raise ValueError(f"Unsupported Obsidian daily profile: {profile_name}") from exc
