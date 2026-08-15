from backend.app.models.affiliate import AffiliateProgram, AffiliateLink

def test_affiliate_program_defaults():
    program = AffiliateProgram(name="Example Network", network="example")
    assert program.name == "Example Network"
    assert program.status == "active"

def test_affiliate_link_defaults():
    link = AffiliateLink(program_id=1, url="https://example.com")
    assert link.clicks == 0
    assert link.conversions == 0
