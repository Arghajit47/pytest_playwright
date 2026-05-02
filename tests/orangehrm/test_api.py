from constants.api_constants import APIEndpoints
import pytest

pytestmark = pytest.mark.usefixtures("login_via_api", "request_setup")


def test_api_orangehrm(request_setup, login_via_api):
    # Use the dynamic cookie in Playwright API Request
    response = request_setup.get(
        APIEndpoints.USERS_ENDPOINT,
        headers={"Cookie": f"orangehrm={login_via_api}"},
    )
    assert response.status == 200
    response_data = response.json()
    print(f"API Response: {response_data}")
    assert response_data["meta"]["total"] >= 0
