from backend.app.services.product_engine import build_product
from backend.app.services.export_service import build_manifest
from backend.app.services.seo_service import build_seo

def test_manifest_contains_product_data():
    draft = build_product("organizzare il bilancio familiare", "finanza")
    manifest = build_manifest(draft)
    assert manifest["title"] == draft.title
    assert manifest["category"] == "finanza"
    assert manifest["suggested_price"] == "4.90"

def test_seo_contains_metadata():
    draft = build_product("organizzare il bilancio familiare", "finanza")
    seo = build_seo(draft)
    assert seo["seo_title"]
    assert seo["meta_description"]
    assert seo["primary_keyword"]
    assert seo["keywords"]
