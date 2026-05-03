from pages.dashboard_page import DashboardPage
import pytest

pytestmark = pytest.mark.usefixtures("login", "logout")


def test_login(page, pulse_step) -> None:
    dashboard_page = DashboardPage(page)
    with pulse_step("Verify dashboard page URL and title"):
        dashboard_page.verify_dashboard_page_url_title()
    with pulse_step("Verify dashboard page header"):
        dashboard_page.verify_dashboard_page_header()
