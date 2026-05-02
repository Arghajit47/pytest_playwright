import re  # re is used for regular expressions
from playwright.sync_api import expect  # expect is used for assertions


def waitForFullyPageLoad(page):
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("load")


# Function name starts with test_ so that pytest will detect it.
# page is automatically injected from Playwright, automatically using the pre instantiated browser (This is possibly because pytest-playwright provides a built-in page fixture)


def test_pulse_report_search(page):
    page.goto(
        "https://arghajit47.github.io/playwright-pulse/"
    )  # This loads pulse report documentation
    waitForFullyPageLoad(page)
    page.locator('[id="searchInput"]').type("Arghajit Singha")
    page.locator('[id="searchInput"]').press("Enter")
    waitForFullyPageLoad(page)
    try:
        page.get_by_role("button", name="Accept All").click(timeout=1000)
    except:
        print("No cookie banner found")
    word_locator = page.locator('[id="support-credits"] h2').first
    print(word_locator.inner_text())
    print(page.title())
    expect(word_locator).to_have_text("Support & Credits")
    expect(page).to_have_title(re.compile("Changelog", re.IGNORECASE))
    page.close()
