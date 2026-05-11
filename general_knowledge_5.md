# Retries in Pytest Playwright

To add retries to your pytest suite, the industry standard is using the **pytest-rerunfailures** plugin. It handles flaky tests (like your tab synchronization issue) by automatically re-running failed tests a specified number of times before marking them as failed.

## 1. Installation

First, install the plugin via pip:

```bash
pip install pytest-rerunfailures

```

---

### 2. Global Retries (Command Line)

If you want **every** test in your suite to retry upon failure, use the `--reruns` flag when executing pytest.

- **Command:** `pytest --reruns 3`
- **With Delay:** `pytest --reruns 3 --reruns-delay 1` (waits 1 second between attempts)

This is the most common approach for CI/CD pipelines where network or browser latency might cause occasional hiccups.

---

### 3. Targeted Retries (Decorators)

If you only have a few specific tests that are "flaky" (like the `test_flaky_orangehrm` test you showed earlier), it is better to target them specifically using a decorator. This prevents wasting time re-running tests that are broken due to actual bugs.

```python
import pytest

@pytest.mark.flaky(reruns=5, reruns_delay=2)
def test_orangehrm_social_link(page):
    # Your test code here
    ...

```

---

### 4. How Retries Look in the Terminal

When a test fails and then passes on a retry, pytest marks it as **R** (Rerun) rather than **F** (Fail) or **.** (Pass).

| Status   | Meaning                                       |
| -------- | --------------------------------------------- |
| `R`      | The test failed but is being re-run.          |
| `PASSED` | The test passed on one of the retry attempts. |
| `FAILED` | The test failed all allocated retry attempts. |

---

### 5. Advanced: Retrying Only Specific Errors

You can be even more surgical by only retrying when a specific error occurs (like an `AssertionError` or a Playwright `TimeoutError`). This ensures that if your code has a `SyntaxError` or `NameError`, it fails immediately without wasting time.

```python
# Only retry if it's an AssertionError
@pytest.mark.flaky(reruns=3, condition=lambda: True, only_rerun=["AssertionError"])
def test_specific_error(page):
    ...

```

### A Quick Note on "Flakiness"

While retries are a great safety net, they often hide underlying synchronization issues. In your specific case with the OrangeHRM tabs, combining **retries** with the `context.expect_page()` pattern I mentioned earlier will make your test suite almost bulletproof.

Do you want to see how to configure these retries automatically in a `pytest.ini` file so you don't have to type the command every time?
