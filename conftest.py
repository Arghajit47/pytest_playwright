from api.base_api import BaseAPI
from constants.api_constants import APIEndpoints
from api.orangehrm_api_auth import OrangeHRMAPI
from constants.common_constants import Cookies
from pages.base_page import BasePage
from pages import base_page
from constants.dashboard_page_constants import DashboardPageConstants
from pages.orangeHRM_login_page import LoginPage
import pytest
import os
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv


# @pytest.fixture(scope="session")
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=True)
#         yield browser
#         browser.close()


# @pytest.fixture
# def page(browser):
#     page = browser.new_page()
#     yield page
#     page.close()


@pytest.fixture(scope="function")
def login(page, pulse_step):
    login_page = LoginPage(page)
    with pulse_step("Navigate to the login page"):
        login_page.go_to_login_page()
    with pulse_step("Verify orangehrm logo is visible"):
        login_page.verify_orangehrm_logo_is_visible()
    creds = login_page.fetch_demo_credentials()
    with pulse_step("Login"):
        login_page.login(creds[0], creds[1])
    print("User is logged in to the OrangeHRM Demo page.")
    yield


@pytest.fixture(scope="function")
def logout(page, pulse_step):
    yield
    login_page = LoginPage(page)
    with pulse_step("Click logout button"):
        login_page.click_logout_button()
    print("User is logged out of the OrangeHRM Demo page.")


@pytest.fixture(scope="function")
def login_via_cookies(page, pulse_step, login_via_api):
    with pulse_step("Store cookies in browser"):
        page.context.add_cookies(
            [
                {
                    "name": Cookies.ORANGEHRM_COOKIE.value,
                    "value": login_via_api,
                    "domain": Cookies.ORANGEHRM_COOKIE_DOMAIN.value,
                    "path": Cookies.ORANGEHRM_COOKIE_PATH.value,
                    "httpOnly": Cookies.ORANGEHRM_COOKIE_HTTPONLY.value,
                    "secure": Cookies.ORANGEHRM_COOKIE_SECURE.value,
                    "sameSite": Cookies.ORANGEHRM_COOKIE_SAMESITE.value,
                }
            ]
        )
    with pulse_step("Navigate to the dashboard page"):
        base_page = BasePage(page)
        base_page.navigateToUrl(DashboardPageConstants.DASHBOARD_PAGE_URL)
        base_page.waitForFullyPageLoad()


@pytest.fixture(scope="function")
def login_via_api(pulse_step):
    with pulse_step("Fetch cookies from API"):
        # Dynamically fetch the authenticated cookie using our Requests utility
        api_auth = OrangeHRMAPI(APIEndpoints.BASE_URL)
        cookie_value = api_auth.login(APIEndpoints.USER_NAME, APIEndpoints.PASSWORD)
        assert cookie_value is not None, "Failed to authenticate and get cookie"
    return cookie_value


@pytest.fixture(scope="function")
def request_setup(playwright, pulse_step):
    with pulse_step("Create request context"):
        request = playwright.request.new_context()
    yield request
    with pulse_step("Dispose request context"):
        request.dispose()
    print("Request is done successfully!")


@pytest.fixture(scope="function")
def base_api_setup(request_setup, pulse_step):
    with pulse_step("Create base api setup"):
        base_api = BaseAPI(request_setup)
    yield base_api


@pytest.fixture(scope="function")
def authentication_token(request_setup, base_api_setup, pulse_step):
    with pulse_step("Fetch authentication token from API"):
        response = base_api_setup.post_response(
            request_setup,
            APIEndpoints.DUMMYJSON_LOGIN_ENDPOINT,
            data={
                "username": os.getenv("DUMMYJSON_USERNAME"),
                "password": os.getenv("DUMMYJSON_PASSWORD"),
            },
            headers={"Content-Type": "application/json"},
        )
    return response["accessToken"]


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    load_dotenv()  # loads environment variables from .env file
    # This runs ONCE in the main master process before workers start
    print("Executing Global Setup and It also sets up the dotenv files")


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """
    # This runs ONCE after all workers have finished
    print("Executing Global Teardown")
