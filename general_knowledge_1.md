# Troubleshooting: Playwright Sync API inside the asyncio loop

## Problem Statement

When running Playwright tests using `pytest`, you might encounter the following fatal error during test setup:

```text
playwright._impl._errors.Error: It looks like you are using Playwright Sync API inside the asyncio loop.
Please use the Async API instead.
```

This error commonly surfaces when you are using the `pytest-playwright` plugin but simultaneously trying to manually define your own core Playwright fixtures (like `browser` or `page`) using `sync_playwright()` inside your `conftest.py`.

## Root Cause Analysis

The `pytest-playwright` plugin is designed to seamlessly integrate Playwright into your pytest execution flow. Out of the box, it automatically handles the lifecycle of the browser and provides its own built-in fixtures, including:

- `browser`
- `context`
- `page`
- `playwright`

Behind the scenes, `pytest-playwright` spins up an internal `asyncio` event loop to manage browser communication efficiently, even if you are writing your test code synchronously.

When you manually override these fixtures in `conftest.py` like this:

```python
# ANTI-PATTERN: Manually overriding pytest-playwright's built-in fixtures
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:  # <-- Conflict!
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()
```

...the manual call to `sync_playwright()` attempts to start a **new** synchronous execution environment. However, because the `pytest-playwright` plugin has already initialized its own event loop for the test session, Playwright detects that you are trying to nest a synchronous Playwright context inside an existing asynchronous event loop and throws an error to prevent deadlocks and unpredictable behavior.

## Solution

**Do not redefine the default fixtures.**

Remove any custom `browser`, `context`, or `page` fixture definitions from your `conftest.py`.

By removing the manual overrides, your tests will fall back to using `pytest-playwright`'s robust built-in fixtures. This not only resolves the event loop collision but also correctly hooks your framework back into `pytest.ini`.

When using the built-in fixtures, you can globally control the browser behavior using `pytest.ini` flags, which is the recommended best practice:

```ini
[pytest]
addopts =  --browser=chromium --tracing=on --screenshot=on --video=on --slowmo=200
```
