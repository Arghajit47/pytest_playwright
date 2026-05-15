from pytest_pulse import pulse_step
from constants.api_constants import APIEndpoints
from constants.components.dashboard.locations_constants import LocationsPageConstants
from locators.components.dashboard.location_locators import LocationsPageLocators
from pages.base_page import BasePage
from pytest_pulse import step


class LocationComponent:
    def __init__(self, page):
        self.page = page
        self.base_page = BasePage(page)

    @step("Verify locations widget text")
    def verify_locations_widget_text(self):
        self.base_page.verify_element_text(
            LocationsPageLocators.LOCATIONS_WIDGET_TEXT,
            LocationsPageConstants.LOCATIONS_WIDGET_TEXT,
        )

    @step("Fetch Data from locations api")
    def get_locations_data(self, request_setup, login_via_api):
        response = request_setup.get(
            APIEndpoints.DASHBOARD_EMPLOYEE_BY_LOCATION,
            headers={"Cookie": f"orangehrm={login_via_api}"},
        )
        return response

    @step("Validate locations data from api")
    def validate_locations_data(self, response):
        response_json = response.json()
        with pulse_step("Verify data section of locations api"):
            if response_json["data"] == []:
                print("No locations data found")
            else:
                print("Locations data found!")
                print(response_json["data"])
            for item in response_json["data"]:
                self.base_page.verify_element_is_visible(
                    LocationsPageLocators.LOCATIONS_LEGENDS(item["location"]["name"]),
                )

        with pulse_step("Verify meta section of locations api"):
            if (
                response_json["meta"] == []
                or response_json["meta"]["unassignedEmployeeCount"] == 0
            ):
                print("No meta data found")
            else:
                print("Meta data found!")
                print(response_json["meta"])
                self.base_page.verify_element_is_visible(
                    LocationsPageLocators.LOCATIONS_LEGENDS("Unassigned"),
                )

        with pulse_step("Verify pie chart of locations api"):
            self.base_page.verify_element_is_visible(
                LocationsPageLocators.LOCATIONS_PIE_CHART
            )
