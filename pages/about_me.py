from constants.about_me_constants import AboutMeAPIResponseKeys
from constants.api_constants import APIEndpoints
from constants.about_me_constants import ABOUT_ME_MODAL_HEADER_TEXT
from constants.about_me_constants import AboutMeKeys
from locators.about_me_locators import AboutMeLocators
from locators.orangeHRM_login_locators import LoginPageLocators
from pages.base_page import BasePage
from api.base_api import BaseAPI
from utils.ui_helpers import UIHelpers
from pytest_pulse import step, pulse_step


class AboutMePage:

    def __init__(self, page):
        self.page = page
        self.base_page = BasePage(page)
        self.base_api = BaseAPI(page)
        self.ui_helpers = UIHelpers(page)

    @step("Click on User Avatar")
    def click_on_user_avatar(self):
        with pulse_step("Click on the user dropdown button"):
            self.base_page.click(LoginPageLocators.USER_DROPDOWN)
        with pulse_step("Verify about me button is visible"):
            self.base_page.verify_element_text(
                AboutMeLocators.ABOUT_ME_BUTTON, ABOUT_ME_MODAL_HEADER_TEXT
            )
        with pulse_step("Click on about me button"):
            self.base_page.click(AboutMeLocators.ABOUT_ME_BUTTON)

    @step("Verify About Me Modal Details")
    def verify_about_me_modal_details(self, request_setup, login_via_api):
        with pulse_step("Get response from API"):
            api_response = self.base_api.get_response(
                request_setup,
                APIEndpoints.ABOUT_ME_API_ENDPOINT,
                headers={"Cookie": f"orangehrm={login_via_api}"},
            )
            # OrangeHRM API v2 often wraps the result in a 'data' key
            api_data = api_response.get("data", api_response)

        with pulse_step("Extract UI data from modal"):
            ui_keys = self.base_page.get_all_element_texts(
                AboutMeLocators.ABOUT_ME_MODAL_KEY_FIELDS
            )
            ui_values = self.base_page.get_all_element_texts(
                AboutMeLocators.ABOUT_ME_MODAL_VALUE_FIELDS
            )
            ui_data = dict(zip(ui_keys, ui_values))

        with pulse_step("Construct expected UI data from API response"):
            expected_ui_data = {
                AboutMeKeys.COMPANY_NAME.value: api_data.get(
                    AboutMeAPIResponseKeys.COMPANY_NAME.value
                ),
                AboutMeKeys.VERSION.value: f"{api_data.get(AboutMeAPIResponseKeys.PRODUCT_NAME.value)} {api_data.get(AboutMeAPIResponseKeys.VERSION.value)}",
                AboutMeKeys.ACTIVE_EMPLOYEES.value: str(
                    api_data.get(AboutMeAPIResponseKeys.ACTIVE_EMPLOYEES.value)
                ),
                AboutMeKeys.EMPLOYEES_TERMINATED.value: str(
                    api_data.get(AboutMeAPIResponseKeys.EMPLOYEES_TERMINATED.value)
                ),
            }

        with pulse_step("Compare UI data with expected API data"):
            for key, expected_value in expected_ui_data.items():
                actual_value = ui_data.get(key)
                with pulse_step(
                    f"Verifying {key}: Expected='{expected_value}', Actual='{actual_value}'"
                ):
                    assert (
                        actual_value == expected_value
                    ), f"Validation failed for {key}. Expected {expected_value} but got {actual_value}"

    @step("Close About Me Modal")
    def close_about_me_modal(self):
        with pulse_step("Click on close button"):
            self.base_page.click(AboutMeLocators.ABOUT_ME_MODAL_CLOSE_BTN)
        with pulse_step("Verify about me modal is hidden"):
            self.base_page.verify_element_is_not_visible(AboutMeLocators.ABOUT_ME_MODAL)
