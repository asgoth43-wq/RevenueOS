from decimal import Decimal
from backend.app.services.dashboard_service import build_summary

def test_dashboard_summary():
    result = build_summary([
        {"revenue": Decimal("10"), "clicks": 100, "conversions": 5},
        {"revenue": Decimal("4.50"), "clicks": 50, "conversions": 5},
    ])
    assert result["items"] == 2
    assert result["revenue"] == Decimal("14.50")
    assert result["clicks"] == 150
    assert result["conversions"] == 10
    assert result["conversion_rate"] == 6.67
