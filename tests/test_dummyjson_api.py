from constants.api_constants import APIEndpoints
import pytest
from pytest_pulse import pulse_step

pytestmark = pytest.mark.usefixtures(
    "authentication_token", "request_setup", "base_api_setup"
)


@pytest.mark.pulse_severity("Medium")
@pytest.mark.pulse_tag("API")
def test_api_authenticated_user(request_setup, authentication_token, base_api_setup):
    # Use the dynamic cookie in Playwright API Request
    with pulse_step("Get response from API"):
        response = base_api_setup.get_response(
            request_setup,
            APIEndpoints.DUMMYJSON_AUTHENTICATION_ENDPOINT,
            headers={"Authorization": f"Bearer {authentication_token}"},
        )
    print(f"API Response: {response}")
    with pulse_step("Assert API Response"):
        assert response["email"] == "emily.johnson@x.dummyjson.com"
