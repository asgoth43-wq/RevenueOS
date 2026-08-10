from backend.app.services.product_engine import build_product

def test_build_product():
    draft = build_product("organizzare il bilancio familiare", "finanza")
    assert draft.title.startswith("Guida pratica:")
    assert draft.category == "finanza"
    assert len(draft.sections) >= 5
    assert draft.suggested_price > 0
