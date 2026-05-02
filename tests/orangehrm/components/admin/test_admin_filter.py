import pytest
from pages.components.admin.system_user_filter_components import (
    SystemUserFilterComponents,
)


pytestmark = pytest.mark.usefixtures(
    "login_via_api", "login_via_cookies", "request_setup"
)


def test_admin_filter(page, request_setup, login_via_api):
    system_user_filter_component = SystemUserFilterComponents(page)
    system_user_filter_component.verify_and_click_on_admin_option()
    system_user_filter_component.verify_admin_page_url()
    response = system_user_filter_component.get_user_list(request_setup, login_via_api)
    print(response)
    system_user_filter_component.verify_user_list(response)
