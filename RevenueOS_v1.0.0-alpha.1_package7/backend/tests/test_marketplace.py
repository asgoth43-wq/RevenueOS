from backend.app.services.product_engine import build_product
from backend.app.services.marketplace_service import add_tracking, build_listing

def test_listing_for_etsy():
    draft = build_product("organizzare il bilancio familiare", "finanza")
    listing = build_listing(draft, "etsy", "https://example.com/product")
    assert listing.marketplace == "etsy"
    assert listing.title
    assert listing.price == "4.90"

def test_tracking_url():
    result = add_tracking("https://example.com/product", "etsy", "budget-guide")
    assert "utm_source=etsy" in result
    assert "utm_medium=marketplace" in result
    assert "utm_campaign=budget-guide" in result
