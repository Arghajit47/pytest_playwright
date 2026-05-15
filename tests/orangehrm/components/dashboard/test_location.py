from pages.components.dashboard.location_components import LocationComponent
import pytest
from pytest_pulse import pulse_step, step

pytestmark = pytest.mark.usefixtures(
    "login_via_api", "login_via_cookies", "request_setup"
)


@pytest.mark.pulse_severity("Medium")
@pytest.mark.pulse_tag("Regression")
@pytest.mark.pulse_tag("Dashboard")
@pytest.mark.pulse_tag("Location")
@step("Test dashboard 'Employee Distribution by Location' widget")
def test_location_component(page, request_setup, login_via_api):
    with pulse_step("Instantiate Location Component"):
        location_component = LocationComponent(page)
    with pulse_step("Verify Location widget text"):
        location_component.verify_locations_widget_text()
    with pulse_step("Get Location Items from API"):
        response = location_component.get_locations_data(request_setup, login_via_api)
    print(f"API Response: {response}")
    with pulse_step("Validate Location Items"):
        location_component.validate_locations_data(response)
