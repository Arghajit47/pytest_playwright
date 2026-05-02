# This is a normal playwright test, not pytest-playwright


from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://google.com")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(15000)
    print(page.title())
    page.close()
    browser.close()
