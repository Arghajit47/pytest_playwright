from pytest_pulse import pulse_step
from constants.api_constants import APIEndpoints
from constants.components.dashboard.subunits_constants import SubunitsPageConstants
from locators.components.dashboard.subnit_locators import SubnitLocators
from pages.base_page import BasePage
from pytest_pulse import step


class SubunitComponent:
    def __init__(self, page):
        self.page = page
        self.base_page = BasePage(page)

    @step("Verify subunit widget text")
    def verify_subunit_widget_text(self):
        self.base_page.verify_element_text(
            SubnitLocators.SUBUNIT_WIDGET_TEXT,
            SubunitsPageConstants.SUBUNIT_WIDGET_TEXT,
        )

    @step("Fetch Data from sub-unit api")
    def get_subunit_data(self, request_setup, login_via_api):
        response = request_setup.get(
            APIEndpoints.DASHBOARD_EMPLOYEE_SUBUNIT,
            headers={"Cookie": f"orangehrm={login_via_api}"},
        )
        return response

    @step("Validate subunit data from api")
    def validate_subunit_data(self, response):
        response_json = response.json()
        with pulse_step("Verify data section of subunit api"):
            if response_json["data"] == []:
                print("No subunit data found")
            else:
                print("Subunit data found!")
                print(response_json["data"])
            for item in response_json["data"]:
                self.base_page.verify_element_is_visible(
                    SubnitLocators.SUBUNIT_LEGENDS(item["subunit"]["name"]),
                )

        with pulse_step("Verify meta section of subunit api"):
            if (
                response_json["meta"] == []
                or response_json["meta"]["unassignedEmployeeCount"] == 0
            ):
                print("No meta data found")
            else:
                print("Meta data found!")
                print(response_json["meta"])
                self.base_page.verify_element_is_visible(
                    SubnitLocators.SUBUNIT_LEGENDS("Unassigned"),
                )

        with pulse_step("Verify pie chart of subunit api"):
            self.base_page.verify_element_is_visible(SubnitLocators.SUBUNIT_PIE_CHART)
