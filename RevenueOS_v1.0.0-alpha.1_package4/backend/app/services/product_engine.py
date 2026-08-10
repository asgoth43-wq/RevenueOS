from dataclasses import dataclass
from decimal import Decimal
import re

@dataclass
class ProductDraft:
    title: str
    category: str
    description: str
    sections: list[str]
    tags: list[str]
    suggested_price: Decimal

def _clean(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()

def build_product(topic: str, category: str = "digital-product") -> ProductDraft:
    topic = _clean(topic)
    category = _clean(category) or "digital-product"
    if len(topic) < 3:
        raise ValueError("topic must contain at least 3 characters")

    title = f"Guida pratica: {topic}"
    description = (
        f"Una guida pratica e organizzata su {topic}, pensata per trasformare "
        "un argomento complesso in passi semplici e applicabili."
    )
    sections = [
        "Introduzione",
        f"Concetti fondamentali di {topic}",
        "Procedura passo per passo",
        "Checklist operativa",
        "Errori comuni da evitare",
        "Piano d'azione",
        "Conclusioni",
    ]
    words = [w.lower() for w in re.findall(r"[A-Za-zÀ-ÿ0-9]+", topic) if len(w) >= 4]
    tags = list(dict.fromkeys(words[:8] + ["guida", "checklist", "template"]))
    return ProductDraft(
        title=title,
        category=category,
        description=description,
        sections=sections,
        tags=tags,
        suggested_price=Decimal("4.90"),
    )
