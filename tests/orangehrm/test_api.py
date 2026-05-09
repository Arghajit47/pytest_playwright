from constants.api_constants import APIEndpoints
import pytest

pytestmark = pytest.mark.usefixtures("login_via_api", "request_setup", "base_api_setup")


@pytest.mark.pulse_severity("Critical")
@pytest.mark.pulse_tag("API")
def test_api_orangehrm(request_setup, login_via_api, base_api_setup):
    # Use the dynamic cookie in Playwright API Request
    response = base_api_setup.get_response(
        request_setup,
        APIEndpoints.USERS_ENDPOINT,
        headers={"Cookie": f"orangehrm={login_via_api}"},
    )
    print(f"API Response: {response}")
    assert response["meta"]["total"] >= 0
