from constants.api_constants import APIEndpoints
from pages.base_page import BasePage
from constants.components.dashboard.quick_launch_constants import (
    QuickLaunchPageConstants,
)
from locators.components.dashboard.quick_launch_locators import QuickLaunchLocators


class QuickLaunchComponent:
    def __init__(self, page):
        self.page = page
        self.base_page = BasePage(page)

    def verify_quick_launch_widget_text(self):
        self.base_page.verify_element_text(
            QuickLaunchLocators.QUICK_LAUNCH_WIDGET_TEXT,
            QuickLaunchPageConstants.QUICK_LAUNCH_WIDGET_TEXT,
        )

    def get_quick_launch_items(self, request_setup, login_via_api):
        response = request_setup.get(
            APIEndpoints.SHORTCUTS_ENDPOINT,
            headers={"Cookie": f"orangehrm={login_via_api}"},
        )
        assert response.status == 200
        return response.json()

    def validate_quick_launch_items(self, response):
        if response["data"] == []:
            print("No items in quick launch")
        else:
            print("Items in quick launch found!")
            print(response["data"])
            data = response.get("data", {})
            if data.get("leave.assign_leave"):
                self.base_page.verify_element_is_visible(
                    QuickLaunchLocators.ASSIGN_LEAVE,
                )
            if data.get("leave.leave_list"):
                self.base_page.verify_element_is_visible(
                    QuickLaunchLocators.LEAVE_LIST,
                )
            if data.get("time.employee_timesheet"):
                self.base_page.verify_element_is_visible(
                    QuickLaunchLocators.MY_TIMESHEETS,
                )
            if data.get("leave.apply_leave"):
                self.base_page.verify_element_is_visible(
                    QuickLaunchLocators.APPLY_LEAVES,
                )
            if data.get("leave.my_leave"):
                self.base_page.verify_element_is_visible(
                    QuickLaunchLocators.MY_LEAVE,
                )
            if data.get("time.my_timesheet"):
                self.base_page.verify_element_is_visible(
                    QuickLaunchLocators.MY_TIMESHEET,
                )
