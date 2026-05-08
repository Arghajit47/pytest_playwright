# Worker management (pytest-xdist)

1. **Install the plugin:**
   Run this in your terminal:

   ```bash
   pip install pytest-xdist
   ```

2. **Verify the installation:**
   Check if pytest now recognizes the xdist hooks:

```bash
   pytest --trace-config | grep xdist
```

3. **Check your `pytest.ini` syntax:**
   In your `pytest.ini`, make sure the syntax is correct. Using a space instead of an `=` for the `-n` flag is generally safer in the config file:

```ini
   [pytest]
   addopts = -n 4 --pulse-report --browser=chromium --html=reports/report.html
```
