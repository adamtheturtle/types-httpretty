from pathlib import Path

import httpretty


def test_stub_package_contains_no_runtime_python() -> None:
    root = Path(__file__).parents[1] / "httpretty-stubs"
    assert not list(root.glob("*.py"))


def test_runtime_smoke() -> None:
    with httpretty.enabled(allow_net_connect=False):
        httpretty.register_uri(httpretty.GET, "https://example.com", body="ok")
