from backend.app.services.analytics_service import revenue_summary, conversion_rate

def test_revenue():
    data = [
        {"source":"gumroad","amount":10},
        {"source":"etsy","amount":5}
    ]
    result = revenue_summary(data)
    assert result["total_revenue"] == 15

def test_conversion():
    assert conversion_rate(100, 5) == 5.0
