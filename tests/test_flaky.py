import pytest
import os
from playwright.sync_api import Page
from pytest_pulse import step, pulse_step

# Path for a persistent counter to track attempts across reruns
COUNTER_FILE = "flaky_counter.tmp"


def get_and_increment_attempt():
    count = 0
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "r") as f:
            try:
                count = int(f.read())
            except ValueError:
                count = 0
    count += 1
    with open(COUNTER_FILE, "w") as f:
        f.write(str(count))
    return count


@pytest.mark.pulse_tag("Regression")
@pytest.mark.pulse_tag("Flaky")
@pytest.mark.flaky(reruns=5, reruns_delay=1)  # Automatically rerun up to 5 times
@step("Test social media link (Flaky Demo)")
def test_flaky_orangehrm_social_link(page: Page):
    # Get current attempt number
    attempt = get_and_increment_attempt()

    with pulse_step("Navigate to the Login page"):
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Use the expect_page() pattern
    with page.context.expect_page() as new_page_info:
        with pulse_step("Click on the LinkedIn icon"):
            page.locator("a[href*='linkedin']").click()

    new_page = new_page_info.value

    # FORCED FLAKINESS: Fail for the first 2 attempts, pass on the 3rd
    with pulse_step(f"Assert number of tabs (Attempt: {attempt})"):
        if attempt < 3:
            assert (
                False
            ), f"Simulated failure on attempt {attempt}. Report should show this as FLAKY."
        else:
            # Clean up the counter file on success so the next test run starts fresh
            if os.path.exists(COUNTER_FILE):
                os.remove(COUNTER_FILE)
            assert True, "Successfully reached the pass attempt!"

    with pulse_step("Assert that the URL contains linkedin"):
        # wait for the new page to actually load
        new_page.wait_for_load_state("networkidle")
        assert "linkedin" in new_page.url.lower()
