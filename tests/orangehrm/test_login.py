from pages.dashboard_page import DashboardPage
import pytest
from pytest_pulse import pulse_step

pytestmark = pytest.mark.usefixtures("login", "logout")


@pytest.mark.pulse_severity("Critical")
@pytest.mark.pulse_tag("Regression")
@pytest.mark.pulse_tag("Login")
def test_login(page, pulse_attach) -> None:
    with pulse_step("Instantiate Dashboard Page"):
        dashboard_page = DashboardPage(page)
    with pulse_step("Verify dashboard page URL and title"):
        dashboard_page.verify_dashboard_page_url_title()
    with pulse_step("Verify dashboard page header"):
        dashboard_page.verify_dashboard_page_header()
    with pulse_step("Capture screenshot and Attach screenshot to report"):
        dashboard_page.capture_dashboard_screenshot_and_attach_to_report(pulse_attach)
