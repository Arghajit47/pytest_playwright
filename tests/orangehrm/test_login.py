from pages.dashboard_page import DashboardPage
import pytest

pytestmark = pytest.mark.usefixtures("login", "logout")


def test_login(page) -> None:
    dashboard_page = DashboardPage(page)
    dashboard_page.verify_dashboard_page_url_title()
    dashboard_page.verify_dashboard_page_header()
