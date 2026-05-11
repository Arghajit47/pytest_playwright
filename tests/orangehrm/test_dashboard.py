import pytest
from pages.dashboard_page import DashboardPage
from pytest_pulse import pulse_step

pytestmark = pytest.mark.usefixtures("login_via_cookies")


@pytest.mark.pulse_severity("High")
@pytest.mark.pulse_tag("Regression")
def test_dashboard_page(page) -> None:
    with pulse_step("Instantiate Dashboard Page"):
        dashboard_page = DashboardPage(page)
    with pulse_step("Verify dashboard page url and title"):
        dashboard_page.verify_dashboard_page_url_title()
    with pulse_step("Verify dashboard page header"):
        dashboard_page.verify_dashboard_page_header()
    with pulse_step("Verify upgrade button is visible"):
        dashboard_page.verify_upgrade_button_is_visible()
    with pulse_step("Verify dashboard widgets count"):
        dashboard_page.verify_dashboard_widgets_count()
    with pulse_step("Verify dashboard widgets texts"):
        dashboard_page.verify_dashboard_widgets_texts()
    with pulse_step("Verify profile image src"):
        dashboard_page.verify_profile_image_src()
