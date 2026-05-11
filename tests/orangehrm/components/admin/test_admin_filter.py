import pytest
from pages.components.admin.system_user_filter_components import (
    SystemUserFilterComponents,
)
from pytest_pulse import step, pulse_step


pytestmark = pytest.mark.usefixtures(
    "login_via_api", "login_via_cookies", "request_setup"
)


@pytest.mark.pulse_severity("High")
@pytest.mark.pulse_tag("Regression")
@pytest.mark.pulse_tag("Admin")
@step("Verify and test admin filter")
def test_admin_filter(page, request_setup, login_via_api):
    with pulse_step("Instantiate System User Filter Components"):
        system_user_filter_component = SystemUserFilterComponents(page)
    with pulse_step("Verify and click on admin option"):
        system_user_filter_component.verify_and_click_on_admin_option()
    with pulse_step("Verify admin page url"):
        system_user_filter_component.verify_admin_page_url()
    with pulse_step("Get user list"):
        response = system_user_filter_component.get_user_list(
            request_setup, login_via_api
        )
    print(response)
    with pulse_step("Verify user list"):
        system_user_filter_component.verify_user_list(response)
