from pages.components.dashboard.subunit_components import SubunitComponent
import pytest
from pytest_pulse import pulse_step, step

pytestmark = pytest.mark.usefixtures(
    "login_via_api", "login_via_cookies", "request_setup"
)


@pytest.mark.pulse_severity("Medium")
@pytest.mark.pulse_tag("Regression")
@pytest.mark.pulse_tag("Dashboard")
@pytest.mark.pulse_tag("Subunit")
@step("Test dashboard 'Employee Distribution by Sub Unit' widget")
def test_subunit_component(page, request_setup, login_via_api):
    with pulse_step("Instantiate Subunit Component"):
        subunit_component = SubunitComponent(page)
    with pulse_step("Verify Subunit widget text"):
        subunit_component.verify_subunit_widget_text()
    with pulse_step("Get Subunit Items from API"):
        response = subunit_component.get_subunit_data(request_setup, login_via_api)
    print(f"API Response: {response}")
    with pulse_step("Validate Subunit Items"):
        subunit_component.validate_subunit_data(response)
