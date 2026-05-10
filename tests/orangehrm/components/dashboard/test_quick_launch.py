from pages.components.dashboard.quick_launch_components import QuickLaunchComponent
import pytest

pytestmark = pytest.mark.usefixtures(
    "login_via_api", "login_via_cookies", "request_setup"
)


@pytest.mark.pulse_severity("Minor")
@pytest.mark.pulse_tag("Regression")
@pytest.mark.pulse_tag("Dashboard")
@pytest.mark.pulse_tag("Quick Launch")
def test_quick_launch_component(page, pulse_step, request_setup, login_via_api):
    # Use the dynamic cookie in Playwright API Request
    quick_launch_component = QuickLaunchComponent(page, pulse_step)
    quick_launch_component.verify_quick_launch_widget_text()
    response = quick_launch_component.get_quick_launch_items(
        request_setup, login_via_api
    )
    print(f"API Response: {response}")
    quick_launch_component.validate_quick_launch_items(response)
