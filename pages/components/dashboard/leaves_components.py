from utils.ui_helpers import UIHelpers
from api.base_api import BaseAPI
from constants.components.dashboard.leaves_constants import LeavesConstants
from locators.components.dashboard.leaves_locators import LeavesLocators
from constants.api_constants import APIEndpoints
from pages.base_page import BasePage
from pytest_pulse import step


class LeavesComponent:

    def __init__(self, page):
        self.page = page
        self.base_page = BasePage(page)
        self.base_api = BaseAPI(page)
        self.ui_helpers = UIHelpers(page)

    @step("Verify leaves widget text")
    def verify_leaves_widget_text(self):
        self.base_page.verify_element_text(
            LeavesLocators.LEAVES_WIDGET_TEXT,
            LeavesConstants.LEAVES_WIDGET_TITLE,
        )
        self.base_page.verify_element_is_visible(LeavesLocators.CONFIGURATION_ICONS)

    @step("Validate no content in leaves widget")
    def validate_no_content_in_leaves_widget(self, request_setup, login_via_api):
        current_date = self.ui_helpers.get_current_date()
        response = self.base_api.get_response(
            request_setup,
            APIEndpoints.DASHBOARD_LEAVES_ENDPOINT(current_date),
            headers={"Cookie": f"orangehrm={login_via_api}"},
        )
        if response.get("data") == []:
            print("No leaves found")
            self.base_page.verify_element_text(
                LeavesLocators.NO_CONTENT_TEXT,
                LeavesConstants.NO_CONTENT_TEXT,
            )
            self.base_page.verify_element_is_visible(LeavesLocators.NO_CONTENT_IMAGE)
