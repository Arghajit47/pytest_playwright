from constants.api_constants import APIEndpoints
import pytest

pytestmark = pytest.mark.usefixtures(
    "authentication_token", "request_setup", "base_api_setup"
)


@pytest.mark.pulse_severity("Medium")
@pytest.mark.pulse_tag("API")
def test_api_authenticated_user(request_setup, authentication_token, base_api_setup):
    # Use the dynamic cookie in Playwright API Request
    response = base_api_setup.get_response(
        request_setup,
        APIEndpoints.DUMMYJSON_AUTHENTICATION_ENDPOINT,
        headers={"Authorization": f"Bearer {authentication_token}"},
    )
    print(f"API Response: {response}")
    assert response["email"] == "emily.johnson@x.dummyjson.com"
