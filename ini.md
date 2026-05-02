# pytest.ini file

The file is the primary configuration file for pytest, allowing you to change the framework's default behavior and standardize test execution across a project. It is typically placed in the project root directory, which pytest then uses to define the for the test run.
Common Uses of [pytest]

• `addopts`: Automatically includes command-line flags (like for verbosity or ) so you don't have to type them every time you run .
• `testpaths`: Specifies which directories pytest should search for tests, speeding up discovery in large projects.
• `markers`: Registers custom markers (e.g., , ) to categorize tests and prevent "unknown marker" warnings.
• `python_files`: Overrides default naming conventions for test discovery (e.g., allowing files ending in to be treated as tests).
• `minversion`: Enforces a minimum version of pytest required to run the suite, ensuring compatibility with specific features.
• `env`: With plugins like pytest-env, you can define runtime environment variables directly in the config file.

Basic Example
A standard starts with a header:

```python
[pytest]
# Add default command line arguments
addopts = -ra -q --tb=short

# Restrict test discovery to these folders
testpaths =
    tests
    integration

# Register custom markers
markers =
    smoke: vital core functionality tests
    slow: tests that take a long time to run
```

## 1. addopts (Additional Options)

This option allows you to pre-define command-line flags so you don't have to type them every time. [2, 3]

- `-ra`: Displays a summary of all test results except passed ones (skipped, failed, etc.).
- `--strict-markers`: Turns "unknown marker" warnings into errors to prevent typos in your test tags.
- `--tb=short`: Shortens the traceback output to just the essential error information. [4, 5]

```python
[pytest]
# Pre-set flags for detailed reporting and safety
addopts = -ra -q --strict-markers --tb=short --cov=myapp
```

## 2. testpaths (Test Discovery)

By default, pytest searches for tests everywhere. testpaths limits this search to specific directories, which significantly speeds up test collection in large repositories. [4, 7, 8, 9, 10]

```python
[pytest]

# Only search these directories for tests

testpaths =
tests
integration_tests
```

## 3. markers (Custom Categories)

Registering markers serves as documentation for your test suite and prevents "UnknownMarkWarning". [11]

- Syntax: marker_name: description.
- Usage: You can then run specific groups using pytest -m smoke. [12, 13, 14]

```python
[pytest]
markers =
smoke: vital core functionality (run with 'pytest -m smoke')
slow: tests that take more than 10 seconds to execute
database: tests requiring an active DB connection
```

## 4. Custom Discovery (python_files, classes, functions) [15, 16, 17]

If your project follows non-standard naming (e.g., using "check" instead of "test"), you can override the discovery patterns. [18]

```python
[pytest]
# Discover files ending in _spec.py
python_files = *_spec.py
# Discover classes starting with 'Check' (e.g., CheckUserLogin)
python_classes = Check*
# Discover functions ending in _verify
python_functions = *_verify
```

## 5. minversion (Compatibility)

Ensures that the environment has a recent enough version of pytest to support the features used in your configuration or tests. [19, 20]

```python
[pytest]
# Force a failure if the runner uses pytest < 7.0
minversion = 7.0
```

## 6. filterwarnings (Cleaning Output)

You can suppress annoying warnings from third-party libraries that you cannot personally fix, keeping your test output clean. [20, 21]

```python
[pytest]
filterwarnings =
ignore::DeprecationWarning
ignore:._Unverified HTTPS request._
```

Key Considerations

• Precedence: `pytest.ini` takes precedence over other configuration files like `pyproject.toml`, `pytest.toml`, or `tox.ini`, even if it is empty.
• Strict Mode: You can use `strict = true` to force the registration of all markers, helping catch typos in test tags early.
• Version Control: This file should always be committed to your repository so that all contributors use the same testing configuration.
