import pytest
from pytest_pulse import step


@pytest.mark.slow
@pytest.mark.pulse_tag("Regression")
@pytest.mark.pulse_tag("Failed")
@pytest.mark.pulse_annotation("Failed test case for report demonstartion")
@pytest.mark.flaky(reruns=2, reruns_delay=1)
@step("Navigate to Google")
def test_failed_action(page, pulse_step):
    with pulse_step("Navigate to Google"):
        page.goto("https://google.com")

    with pulse_step("Search for playwright-pulse"):
        assert "Playwright" in page.title()
