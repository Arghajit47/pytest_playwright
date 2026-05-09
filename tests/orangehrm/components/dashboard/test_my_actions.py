from pages.components.dashboard.my_actions_components import MyActionsComponent
import pytest

pytestmark = pytest.mark.usefixtures(
    "login_via_api", "login_via_cookies", "request_setup"
)


@pytest.mark.pulse_severity("Low")
@pytest.mark.pulse_tag("Regression")
@pytest.mark.pulse_tag("Dashboard")
@pytest.mark.pulse_tag("My Actions")
def test_my_actions_component(page, request_setup, login_via_api):
    # Use the dynamic cookie in Playwright API Request
    my_actions_component = MyActionsComponent(page)
    my_actions_component.verify_my_actions_widget_text()
    response = my_actions_component.get_my_action_items_from_api(
        request_setup, login_via_api
    )
    print(f"API Response: {response}")
    my_actions_component.validate_my_action_items(response)
