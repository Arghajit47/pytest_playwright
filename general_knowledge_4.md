# Use .env files in pytest

To use `.env` files in Pytest, the most reliable and "Pythonic" way is to use the **`python-dotenv`** library. This allows you to load variables from a `.env` file into `os.environ` so they can be accessed anywhere in your automation suite.

## 1. Installation

First, you need to install the library in your virtual environment:

```bash
pip install python-dotenv
```

---

## 2. Create your `.env` file

Place a `.env` file in your project root (same level as your `pytest.ini` and `conftest.py`):

```text
BASE_URL=https://staging.example.com
API_KEY=your_secret_key_123
DB_PASSWORD=admin_pass
```

---

## 3. Load values in `conftest.py`

To make these variables available globally across all your tests, load them inside your `conftest.py` using the `pytest_sessionstart` hook (which we discussed earlier for global setup).

```python
import os
from dotenv import load_dotenv

def pytest_sessionstart(session):
    # Load the .env file at the start of the test session
    load_dotenv()
```

---

## 4. Access values in your Tests

Once loaded, you can access these values using the standard `os.getenv()` method.

**Example Test:**

```python
import os
import pytest
from playwright.sync_api import Page

def test_login_with_env_vars(page: Page):
    # Retrieve values
    base_url = os.getenv("BASE_URL")
    api_key = os.getenv("API_KEY")

    # Use them in your Playwright logic
    page.goto(base_url)
    print(f"Using API Key: {api_key}")
```

---

## 5. Advanced: Creating a Configuration Fixture

Instead of calling `os.getenv` repeatedly in every test, it is a better practice to create a configuration fixture. This keeps your tests clean and provides a single place to handle default values.

In `conftest.py`:

```python
import os
import pytest
from dotenv import load_dotenv

load_dotenv() # Load at the top level of conftest

@pytest.fixture(scope="session")
def env_config():
    return {
        "base_url": os.getenv("BASE_URL", "https://default.com"),
        "api_key": os.getenv("API_KEY"),
        "timeout": int(os.getenv("TIMEOUT", 30000))
    }

# Usage in a test:
def test_example(page: Page, env_config):
    page.goto(env_config["base_url"])
```

## Important Security Tips

- **`.gitignore`**: Always add `.env` to your `.gitignore` file. You should never commit actual secrets (like API keys or passwords) to your repository.
- **`.env.example`**: Create a template file named `.env.example` containing the keys but no values. This helps other team members (or your CI/CD pipeline) know which environment variables are required to run the tests.
