from backend.app.api.version import version

def test_version():
    result = version()
    assert result["name"] == "RevenueOS"
    assert result["version"] == "1.0.0"
    assert result["status"] == "release-candidate"
