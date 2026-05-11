from pages.components.dashboard.quick_launch_components import QuickLaunchComponent
import pytest
from pytest_pulse import pulse_step

pytestmark = pytest.mark.usefixtures(
    "login_via_api", "login_via_cookies", "request_setup"
)


@pytest.mark.pulse_severity("Minor")
@pytest.mark.pulse_tag("Regression")
@pytest.mark.pulse_tag("Dashboard")
@pytest.mark.pulse_tag("Quick Launch")
def test_quick_launch_component(page, request_setup, login_via_api):
    # Use the dynamic cookie in Playwright API Request
    with pulse_step("Instantiate Quick Launch Component"):
        quick_launch_component = QuickLaunchComponent(page)
    with pulse_step("Verify Quick Launch widget text"):
        quick_launch_component.verify_quick_launch_widget_text()
    with pulse_step("Get Quick Launch Items from API"):
        response = quick_launch_component.get_quick_launch_items(
            request_setup, login_via_api
        )
    print(f"API Response: {response}")
    with pulse_step("Validate Quick Launch Items"):
        quick_launch_component.validate_quick_launch_items(response)
