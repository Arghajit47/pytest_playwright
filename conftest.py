from constants.api_constants import APIEndpoints
from utils.api_auth import OrangeHRMAPI
from constants.common_constants import Cookies
from pages.base_page import BasePage
from pages import base_page
from constants.dashboard_page_constants import DashboardPageConstants
from pages.orangeHRM_login_page import LoginPage
import pytest
from playwright.sync_api import sync_playwright


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
def login(page):
    login_page = LoginPage(page)
    login_page.go_to_login_page()
    login_page.verify_orangehrm_logo_is_visible()
    creds = login_page.fetch_demo_credentials()
    login_page.login(creds[0], creds[1])
    print("User is logged in to the OrangeHRM Demo page.")
    yield


@pytest.fixture(scope="function")
def logout(page):
    yield
    login_page = LoginPage(page)
    login_page.click_logout_button()
    print("User is logged out of the OrangeHRM Demo page.")


@pytest.fixture(scope="function")
def login_via_cookies(page, login_via_api):
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
    base_page = BasePage(page)
    base_page.navigateToUrl(DashboardPageConstants.DASHBOARD_PAGE_URL)
    base_page.waitForFullyPageLoad()


@pytest.fixture(scope="function")
def login_via_api():
    # Dynamically fetch the authenticated cookie using our Requests utility
    api_auth = OrangeHRMAPI(APIEndpoints.BASE_URL)
    cookie_value = api_auth.login(APIEndpoints.USER_NAME, APIEndpoints.PASSWORD)
    assert cookie_value is not None, "Failed to authenticate and get cookie"
    return cookie_value


@pytest.fixture(scope="function")
def request_setup(playwright):
    request = playwright.request.new_context()
    yield request
    request.dispose()
    print("Request is done successfully!")
