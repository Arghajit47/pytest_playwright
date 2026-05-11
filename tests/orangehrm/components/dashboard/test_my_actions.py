from pages.components.dashboard.my_actions_components import MyActionsComponent
import pytest
from pytest_pulse import pulse_step

pytestmark = pytest.mark.usefixtures(
    "login_via_api", "login_via_cookies", "request_setup"
)


@pytest.mark.pulse_severity("Low")
@pytest.mark.pulse_tag("Regression")
@pytest.mark.pulse_tag("Dashboard")
@pytest.mark.pulse_tag("My Actions")
def test_my_actions_component(page, request_setup, login_via_api):
    # Use the dynamic cookie in Playwright API Request
    with pulse_step("Instantiate My Actions Component"):
        my_actions_component = MyActionsComponent(page)
    with pulse_step("Verify My Actions widget text"):
        my_actions_component.verify_my_actions_widget_text()
    with pulse_step("Get My Action Items from API"):
        response = my_actions_component.get_my_action_items_from_api(
            request_setup, login_via_api
        )
    print(f"API Response: {response}")
    with pulse_step("Validate My Action Items"):
        my_actions_component.validate_my_action_items(response)
