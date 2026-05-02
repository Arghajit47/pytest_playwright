# GitHub Actions Implementation: Pytest & Playwright

This document outlines the considerations, implementation details, and reasoning behind the `.github/workflows/pytest.yml` configuration created to run your automation suite in the cloud.

## 1. Execution Triggers (`on`)

**What was done:** Configured the workflow to run on `push` and `pull_request` to the `main` and `master` branches, as well as enabling `workflow_dispatch`.
**Why:**

- `push` / `pull_request`: Ensures continuous integration (CI) by automatically verifying that new code changes don't break existing tests before they are merged.
- `workflow_dispatch`: Adds a manual "Run workflow" button in the GitHub Actions UI. This is incredibly useful for triggering on-demand test runs without having to push a dummy code commit.

## 2. Operating System Environment (`runs-on`)

**What was done:** Set the runner to `ubuntu-latest`.
**Why:** Ubuntu is the fastest, most stable, and most cost-effective runner provided by GitHub Actions. Linux environments spin up significantly faster than macOS or Windows runners, saving you CI minutes.

## 3. Python Configuration and Caching

**What was done:** Used `actions/setup-python@v5` with version `3.12` and enabled `cache: 'pip'`.
**Why:**

- Specifying a stable modern version of Python (`3.12`) ensures predictable environments.
- The `cache: 'pip'` directive is crucial for CI performance. It caches your `requirements.txt` dependencies between runs so that subsequent workflow executions don't have to download `playwright` and other packages from scratch every time, saving valuable minutes per run.

## 4. Playwright Browser Installation

**What was done:** Added the command `playwright install --with-deps chromium`.
**Why:**

- **`--with-deps`**: A fresh Ubuntu container lacks many low-level OS packages (like font libraries, graphics drivers, and X11 utilities) required for headless browsers to run. This flag automatically installs all those system-level requirements.
- **`chromium`**: By default, `playwright install` downloads Chromium, Firefox, and WebKit binaries, which can take over a minute. Since your `pytest.ini` specifies `--browser=chromium`, explicitly installing _only_ Chromium drastically cuts down the setup time in CI.

## 5. Test Execution

**What was done:** Simply executed `pytest` without passing manual arguments.
**Why:** Because your framework is already strictly configured via `pytest.ini` (e.g., testpaths, `--tracing=on`, `--alluredir=allure_results`), keeping the CI command clean as just `pytest` ensures a Single Source of Truth. If you change reporting configurations in the future, you only need to modify `pytest.ini`, and the CI will automatically inherit those changes.

## 6. Artifact Uploads & Reporting

**What was done:**

1. Added a step to directly download and install the official Allure binary using `wget`.
2. Executed `allure generate allure_results -o allure-report --clean` to build the HTML report from the raw Pytest data.
3. Configured `actions/upload-artifact@v4` to upload `reports/` (Pytest-HTML), `allure_results/` (Raw Allure JSONs), and `allure-report/` (The generated Allure HTML website). Crucially, I added `if: always()` to these steps.

**Why:**

- **Allure Installation**: The `allure-pytest` pip package ONLY creates the raw JSON files, it does not include the HTML generator CLI. The `allure` CLI is actually a standalone Java application built by Qameta, so it cannot be installed via `pip`. Locally, you use `brew install allure`, but macOS Homebrew is not available on an Ubuntu runner. To avoid bringing in NPM wrappers, we simply download the raw compiled Java binary from their GitHub releases, extract it, and link it to the system path so the CI can run `allure generate`.
- **`if: always()`**: GitHub Actions terminates a job immediately if a step exits with an error code (which `pytest` does when a test fails). By adding `if: always()`, we force GitHub to upload the HTML report, traces, and Allure results **even if the tests fail**.
- Without this, you wouldn't get the Playwright traces or screenshots precisely when you need them most—when a test breaks in CI!
- A `retention-days: 14` limit was added to prevent storage bloat in your GitHub repository while giving you ample time to inspect failed runs.
