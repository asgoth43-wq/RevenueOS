from typing import Any

def build_seo(draft: Any) -> dict:
    primary = draft.tags[0] if draft.tags else draft.category
    return {
        "seo_title": draft.title[:70],
        "meta_description": draft.description[:160],
        "primary_keyword": primary,
        "keywords": draft.tags,
    }
