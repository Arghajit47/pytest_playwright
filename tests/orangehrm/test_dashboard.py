import pytest
from pages.dashboard_page import DashboardPage

pytestmark = pytest.mark.usefixtures("login_via_cookies")


@pytest.mark.pulse_severity("High")
@pytest.mark.pulse_tag("Regression")
def test_dashboard_page(page) -> None:
    dashboard_page = DashboardPage(page)
    dashboard_page.verify_dashboard_page_url_title()
    dashboard_page.verify_dashboard_page_header()
    dashboard_page.verify_upgrade_button_is_visible()
    dashboard_page.verify_dashboard_widgets_count()
    dashboard_page.verify_dashboard_widgets_texts()
    dashboard_page.verify_profile_image_src()
