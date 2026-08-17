from decimal import Decimal

def build_summary(rows: list[dict]) -> dict:
    revenue = sum((Decimal(str(r.get("revenue", 0))) for r in rows), Decimal("0"))
    clicks = sum(int(r.get("clicks", 0)) for r in rows)
    conversions = sum(int(r.get("conversions", 0)) for r in rows)
    conversion_rate = round((conversions / clicks) * 100, 2) if clicks else 0.0
    return {"items": len(rows), "revenue": revenue, "clicks": clicks,
            "conversions": conversions, "conversion_rate": conversion_rate}
