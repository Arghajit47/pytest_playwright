# Playwright with Python

what is playwright?

--> It's a tool to test websites from start to end (like how a user uses it).
It can automate browser actions like clicking, typing, scrolling, etc. It's a
framework for web testing and automation.

## first_test.py

```python
from playwright.sync_api import sync_playwright
# import the sync_playwright function from the playwright.sync_api module,
# which is the tool we use to control the browser in a synchronous way.

with sync_playwright() as p: # create a playwright instance
    # launch the chromium browser in non-headless mode
    browser = p.chromium.launch(headless=False)
    page = browser.new_page() # create a new page
    page.goto("https://google.com") # navigate to the google website
    page.wait_for_load_state("domcontentloaded") # wait for the dom to be loaded
    page.wait_for_timeout(15000) # wait for 15 seconds
    print(page.title()) # print the title of the page
    page.close() # close the page
    browser.close() # close the browser
```

## pytest-playwright

--> pytest-playwright is a plugin for pytest that allows you to use playwright
with pytest. It provides a simple and efficient way to test websites using
pytest. pytest is a testing framework for python - it's used to write simple,
scalable and readble test cases.

## The difference between playwright and pytest-playwright

<!-- markdownlint-disable MD013 -->

| Category                 | Playwright                                                                                                    | Playwright with Pytest                                                                                                                                                                                                                          |
| :----------------------- | :------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Installation command** | `pip3 install playwright`                                                                                     | `pip3 install pytest-playwright`                                                                                                                                                                                                                |
| **Contents**             | Core playwright API                                                                                           | Adds Pytest integration (fixtures, CLI support)                                                                                                                                                                                                 |
| **Description**          | This installs playwright core (including browser automation API and bindings, but not the pytest integration) | This installs the pytest plugin for Playwright. Features: 1. Write tests using pytest structure (`def test_ ...`); 2. Use pytest fixtures (`page`, `browser`, etc.) without manually launching them; 3. Easily run tests with `pytest` command. |

<!-- markdownlint-enable MD013 -->

## Project Structure

Imagine you are testing 10 different websites. Each website has its own set of
test cases. But, all of them has the same browser instance and the same set of
utilities to be used.

```python
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()

...

browser.close()
```

So, you can create a conftest.py file to store the browser instance and the
utilities. And then, you can import the browser instance and the utilities in
your test files.

```python
# conftest.py
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
```

This gives every test a fresh page object and a fresh Chromium browser instance.
Here's the fixture browser:

1. Starts the broswer (Chromium) once per session as the scope is set to "session".
2. yield let the test to use the browser.
3. After the test is done, it closes the browser.

Here's the fixture page:

1. Uses the browser fixture
2. Creates a new browser page for each test
3. yield page gives the test a fresh tab
4. After test, it closes the tab

In your test just call the page fixture:

```python
def test_pulse_report_search(page):
    page.goto(
        "https://arghajit47.github.io/playwright-pulse/"
    )  # This loads pulse report documentation
```

Now, we all remember the best thing about playwright, it's all in one config
file. Just make the configuration there and it will adopt those configurations
by default, right?

But pytest-playwright doesn't have any config file. Here's how to make a
config file for pytest-playwright:

<!-- markdownlint-disable MD013 -->

```python
# pytest.ini
[pytest]
testpaths = tests
addopts = --headless --browser=chromium --slowmo=200 --html=reports/report.html --self-contained-html --trace=on --screenshot=on --video=on
```

<!-- markdownlint-enable MD013 -->

To learn more about pytest.ini file, visit: [ini.md](ini.md)

## Requirements.txt

Requirements.txt is a file that contains the list of all the libraries and
dependencies that are required for the project. It is used to install the
libraries and dependencies in the project.

1. You can see all the libraries installed in the project using the command
   `pip3 freeze` or `pip freeze` (depending on the version of pip installed).

2. To create a requirements.txt file, you can use the command
   `pip3 freeze > requirements.txt` or `pip freeze > requirements.txt`
   (depending on the version of pip installed).

3. You can install all the libraries in the project using the command
   `pip3 install -r requirements.txt` or `pip install -r requirements.txt`.

So a typical project structure would be:

```bash
project-root/
├── tests/                    # All your test files go here
│   ├── test_feature_1.py
│   ├── test_feature_2.py
│   └── test_feature_3.py
├── pages/                  # Page object model
│   ├── base_page.py
│   ├── home_page.py
│   └── search_page.py
├── utils/                  # Utility functions (if needed)
│   ├── base_utils.py
│   ├── home_utils.py
│   └── search_utils.py
├── conftest.py               # Setting up browser and page fixtures for pytest
├── reports/                  # HTML reports are saved here
│   └── report.html
    └── screenshots/          # Screenshots are saved here (optional)
    └── videos/               # Videos are saved here (optional)
    └── traces/               # Traces are saved here (optional)
├── .gitignore                # To exclude node_modules, etc.
├── pytest.ini                # Configuration for pytest
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## How can we record our tests for pytest-playwright?

1. Run the command `playwright codegen <url>`
2. This will open the playwright GUI
3. Click on the record button
4. Record your tests
5. Click on the stop button
6. OPTIONAL:
   Select which test runner you want to generate code in Playwright Pytest/NodeJs/Python.
7. OPTIONAL: Run command
   `playwright codegen https://build.nvidia.com/ --target python3 -o test_script.py`
   This will generate a test script for the URL.
8. Copy the code to your test file
9. Run the test using `pytest`

## How to implement Page Object Model (POM)

POM is a design pattern used in test automation.
It helps you write clean, reusable and maintainable test code.

Each webpage = One class (e.g., LoginPage, HomePage, SearchPage, etc.)
Each class = Methods (actions you can perform on the page) & Locators

Example:

```python
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator('[id="username"]')
        self.password = page.locator('[id="password"]')
        self.login_button = page.locator('[id="login"]')

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
```

How it helps
Reusablity, Readability, Maintainability, Scalability

## Worker management (pytest-xdist)

Check out the [general_knowledge_3.md](general_knowledge_3.md) file for more information.

## Environment Variables

Check out the [general_knowledge_4.md](general_knowledge_4.md) file for more information.
