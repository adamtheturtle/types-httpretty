# types-httpretty

Typing stubs for [HTTPretty](https://github.com/gabrielfalcao/HTTPretty).

```console
python -m pip install types-httpretty
```

The package contains no runtime code. Install `httpretty` separately (or let
your application declare it as its runtime dependency).

The stubs currently target HTTPretty 1.1.4 and require Python 3.10 or newer.

## Development

```console
python -m venv .venv
.venv/bin/pip install '.[dev]'
.venv/bin/pytest
.venv/bin/ruff check .
.venv/bin/ruff format --check .
.venv/bin/mypy tests/typecheck
.venv/bin/pyright tests/typecheck
.venv/bin/python -m mypy.stubtest httpretty --allowlist stubtest_allowlist.txt
.venv/bin/python -m build
.venv/bin/check-wheel-contents dist/*.whl
```

## License

MIT.
