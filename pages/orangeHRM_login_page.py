from constants.dashboard_page_constants import DashboardPageConstants
from constants.login_page_constants import LoginPageConstants
from pages.base_page import BasePage
from locators.orangeHRM_login_locators import LoginPageLocators
from playwright.sync_api import Page
import os
from pytest_pulse import step


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.base_page = BasePage(page)
        self.username_inputbox = page.get_by_role("textbox", name="Username")
        self.password_inputbox = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

    @step("Login to OrangeHRM")
    def login(
        self,
        username: str = os.getenv("USERNAME"),
        password: str = os.getenv("PASSWORD"),
    ):
        self.base_page.fill(self.username_inputbox, username)
        self.base_page.fill(self.password_inputbox, password)
        self.base_page.click(self.login_button)
        self.base_page.waitForFullyPageLoad()

    @step("Enter username")
    def enter_username(self, username: str):
        self.base_page.fill(self.username_inputbox, username)

    @step("Enter password")
    def enter_password(self, password: str):
        self.base_page.fill(self.password_inputbox, password)

    @step("Fetch demo credentials")
    def fetch_demo_credentials(self):
        userName = (
            self.page.locator(LoginPageLocators.USERNAME_DATA)
            .inner_text()
            .split(": ")[1]
            .strip()
        )
        password = (
            self.page.locator(LoginPageLocators.PASSWORD_DATA)
            .inner_text()
            .split(": ")[1]
            .strip()
        )
        return userName, password

    @step("Go to login page")
    def go_to_login_page(self):
        self.base_page.navigateToUrl(LoginPageConstants.LOGIN_PAGE_URL)

    @step("Verify orangehrm logo is visible")
    def verify_orangehrm_logo_is_visible(self):
        self.base_page.verify_element_is_visible(LoginPageLocators.COMPANY_LOGO)

    @step("Verify page header")
    def verify_page_header(self):
        self.base_page.verify_element_is_visible(LoginPageLocators.PAGE_HEADER)
        self.base_page.verify_element_text(
            LoginPageLocators.PAGE_HEADER,
            DashboardPageConstants.DASHBOARD_PAGE_HEADER,
        )

    @step("Click logout button")
    def click_logout_button(self):
        self.base_page.click(LoginPageLocators.USER_DROPDOWN)
        self.base_page.click(LoginPageLocators.LOGOUT_BUTTON)
        self.base_page.waitForFullyPageLoad()
        self.base_page.verify_element_is_visible(self.login_button)
