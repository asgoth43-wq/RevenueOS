from collections import defaultdict

def revenue_summary(items):
    total = sum(float(i.get("amount", 0)) for i in items)
    by_source = defaultdict(float)
    for item in items:
        source = item.get("source", "unknown")
        by_source[source] += float(item.get("amount", 0))
    return {
        "total_revenue": round(total, 2),
        "sources": {k: round(v, 2) for k, v in by_source.items()}
    }

def conversion_rate(clicks: int, conversions: int) -> float:
    if clicks <= 0:
        return 0.0
    return round((conversions / clicks) * 100, 2)
