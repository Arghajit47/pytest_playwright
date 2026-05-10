from pages.dashboard_page import DashboardPage
import pytest

pytestmark = pytest.mark.usefixtures("login", "logout")


@pytest.mark.pulse_severity("Critical")
@pytest.mark.pulse_tag("Regression")
@pytest.mark.pulse_tag("Login")
def test_login(page, pulse_step, pulse_attach) -> None:
    dashboard_page = DashboardPage(page, pulse_step)
    with pulse_step("Verify dashboard page URL and title"):
        dashboard_page.verify_dashboard_page_url_title()
    with pulse_step("Verify dashboard page header"):
        dashboard_page.verify_dashboard_page_header()
    with pulse_step("Capture screenshot and Attach screenshot to report"):
        dashboard_page.capture_dashboard_screenshot_and_attach_to_report(pulse_attach)
