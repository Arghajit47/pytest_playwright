# Pytest General Knowledge

## Using Fixtures as `beforeEach` and `afterEach`

In Pytest, you don't have explicit `beforeEach` or `afterEach` blocks like in other testing frameworks (such as Jest or Mocha). Instead, you use **fixtures** and the `yield` statement to achieve this.

### 1. The `yield` Statement (Setup & Teardown)

Anything you put **before** the `yield` keyword in a fixture runs as setup (`beforeEach`).
Anything you put **after** the `yield` keyword runs as teardown (`afterEach`).

**Example: Setup (`beforeEach`) and Teardown (`afterEach`) in a single fixture**

```python
import pytest

@pytest.fixture(scope="function")
def login_and_logout(page):
    # --- SETUP (Runs BEFORE the test) ---
    login_page = LoginPage(page)
    login_page.login(username, password)

    yield  # The test executes here!

    # --- TEARDOWN (Runs AFTER the test) ---
    login_page.logout()
```

**Example: Pure Teardown (`afterEach`) fixture**
If you want a fixture that _only_ runs teardown logic, simply yield immediately:

```python
@pytest.fixture(scope="function")
def logout(page):
    yield  # Let the test run first

    # --- TEARDOWN (Runs AFTER the test) ---
    login_page = LoginPage(page)
    login_page.logout()
```

### 2. Automatically Applying Fixtures to All Tests in a File

If you want a fixture to automatically run for every single test in a specific file (without having to pass the fixture manually into every test function's arguments), use `pytestmark`.

At the top of your test file, define `pytestmark`:

```python
# test_example.py
import pytest

# This tells Pytest to run the "login" and "logout" fixtures
# automatically for every test in this file.
pytestmark = pytest.mark.usefixtures("login", "logout")

def test_dashboard_access(page):
    # The 'login' setup has already run!
    # The test logic goes here...
    pass
    # The 'logout' teardown will automatically run after this finishes!
```

This is the cleanest way to replicate `beforeEach` and `afterEach` behavior for a suite of tests in Pytest.
