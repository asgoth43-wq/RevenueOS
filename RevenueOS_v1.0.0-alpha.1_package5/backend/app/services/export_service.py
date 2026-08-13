from pathlib import Path
from typing import Any
import json
import re

def safe_filename(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9À-ÿ _-]+", "", value).strip()
    return re.sub(r"\s+", "-", value)[:80] or "product"

def build_manifest(draft: Any) -> dict:
    return {
        "title": draft.title,
        "category": draft.category,
        "description": draft.description,
        "sections": draft.sections,
        "tags": draft.tags,
        "suggested_price": str(draft.suggested_price),
    }

def export_json(draft: Any, output_dir: str = "exports") -> str:
    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{safe_filename(draft.title)}.json"
    path.write_text(json.dumps(build_manifest(draft), ensure_ascii=False, indent=2), encoding="utf-8")
    return str(path)
