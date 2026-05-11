from utils.ui_helpers import UIHelpers
from constants.api_constants import APIEndpoints
from constants.components.admin.system_user_filter_constants import (
    SystemUserFilterConstants,
)
from locators.components.admin.system_user_filter_locators import (
    SystemUserFilterLocators,
)
from pages.base_page import BasePage
from pytest_pulse import step


class SystemUserFilterComponents:

    def __init__(self, page):
        self.page = page
        self.base_page = BasePage(page)
        self.ui_helpers = UIHelpers(page)

    @step("Verify and click on admin option")
    def verify_and_click_on_admin_option(self):
        self.base_page.verify_element_text(
            SystemUserFilterLocators.ADMIN_OPTION,
            SystemUserFilterConstants.ADMIN_OPTION_TEXT,
        )
        self.base_page.click(SystemUserFilterLocators.ADMIN_OPTION)

    @step("Verify admin page url")
    def verify_admin_page_url(self):
        self.base_page.verify_page_url(SystemUserFilterConstants.ADMIN_PAGE_URL)

    @step("Verify user list count")
    def verify_user_list_length(self, response):
        total_count = response["meta"]["total"]
        if total_count == 1:
            self.base_page.verify_element_text(
                SystemUserFilterLocators.USER_LIST_COUNT,
                f"({total_count}) Record Found",
            )
        else:
            self.base_page.verify_element_text(
                SystemUserFilterLocators.USER_LIST_COUNT,
                f"({total_count}) Records Found",
            )
        self.base_page.verify_element_count(
            SystemUserFilterLocators.USER_LIST_ROWS,
            len(response["data"]),
        )

    @step("Get user list")
    def get_user_list(self, request_setup, login_via_api):
        response = request_setup.get(
            APIEndpoints.USERS_ENDPOINT,
            headers={"Cookie": f"orangehrm={login_via_api}"},
        )
        assert response.status == 200
        return response.json()

    @step("Verify user list")
    def verify_user_list(self, response):
        data = response.get("data", [])
        if not data:
            print("No items in user list")
            return

        print("Items in user list found!")
        self.verify_user_list_length(response)

        for i, user in enumerate(data, start=1):
            self.base_page.verify_element_text_ignore_case(
                SystemUserFilterLocators.USER_LIST_CELLS(i, 2),
                user.get("userName", ""),
            )
            self.base_page.verify_element_text_ignore_case(
                SystemUserFilterLocators.USER_LIST_CELLS(i, 3),
                user.get("userRole", {}).get("displayName", ""),
            )

            employee = user.get("employee", {})
            self.base_page.verify_element_text_ignore_case(
                SystemUserFilterLocators.USER_LIST_CELLS(i, 4),
                f"{employee.get('firstName', '')} {employee.get('lastName', '')}".strip(),
            )
            self.base_page.verify_element_text_ignore_case(
                SystemUserFilterLocators.USER_LIST_CELLS(i, 5),
                self.ui_helpers.convert_true_to_enable(user.get("status")),
            )
