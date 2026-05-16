from pytest_pulse import step, pulse_step
from utils.ui_helpers import UIHelpers
from constants.api_constants import APIEndpoints
from constants.components.dashboard.latest_posts_locators import LatestPostsConstants
from locators.components.dashboard.latest_posts_locators import LatestPostsLocators
from pages.base_page import BasePage


class LatestPostsComponent:
    def __init__(self, page):
        self.page = page
        self.base_page = BasePage(page)
        self.ui_helpers = UIHelpers(page)

    @step("Verify latest posts widget header text")
    def verify_latest_posts_widget_text(self):
        self.base_page.verify_element_text(
            LatestPostsLocators.HEADER,
            LatestPostsConstants.LATEST_POSTS_WIDGET_TEXT,
        )

    @step("Fetch latest posts data from API")
    def get_latest_posts_data(self, request_setup, login_via_api):
        response = request_setup.get(
            APIEndpoints.DASHBOARD_LATEST_POSTS,
            headers={"Cookie": f"orangehrm={login_via_api}"},
        )
        return response.json()

    @step("Validate posts user name")
    def validate_posts_user_name(self, data, post_locator):
        with pulse_step("Get user name from API"):
            user_name_locator = post_locator.locator(
                LatestPostsLocators.POSTS_USER_NAME
            )
            first_name = data["employee"]["firstName"]
            middle_name = data["employee"]["middleName"]
            last_name = data["employee"]["lastName"]
        with pulse_step("Generate expected user name"):
            if middle_name:
                expected_name = f"{first_name} {middle_name} {last_name}"
            else:
                expected_name = f"{first_name} {last_name}"
        with pulse_step("Verify user name"):
            self.base_page.verify_element_text(user_name_locator, expected_name)

    @step("Validate posts user image")
    def validate_posts_user_image(self, data, post_locator):
        with pulse_step("Get user image from API Response"):
            user_image_locator = post_locator.locator(
                LatestPostsLocators.POSTS_USER_IMAGE
            )
        with pulse_step("Verify user image"):
            self.base_page.verify_attribute_value_contains(
                user_image_locator,
                "src",
                str(data["employee"]["empNumber"]),
            )

    @step("Validate posts creation date time")
    def validate_posts_creation_date_time(self, data, post_locator):
        with pulse_step("Get creation date time from API Response"):
            creation_time_locator = post_locator.locator(
                LatestPostsLocators.POSTS_CREATION_TIME
            )
        with pulse_step("Verify creation date contains the year"):
            if data.get("createdDate"):
                year = data["createdDate"].split("-")[0]
                self.base_page.verify_element_text_contains(creation_time_locator, year)

    @step("Validate latest posts data")
    def validate_latest_posts_data(self, response_json):
        with pulse_step("Verify latest posts data"):
            if response_json["data"] == []:
                print("No latest posts data found")
            else:
                print("Latest posts data found!")
                self.base_page.verify_element_count(
                    LatestPostsLocators.POSTS_CONTAINER, len(response_json["data"])
                )
            with pulse_step("Validate posts data"):
                for index, item in enumerate(response_json["data"]):
                    post_locator = self.page.locator(
                        LatestPostsLocators.POSTS_CONTAINER
                    ).nth(index)
                    self.validate_posts_user_name(item, post_locator)
                    self.validate_posts_user_image(item, post_locator)
                    self.validate_posts_creation_date_time(item, post_locator)
                    self.validate_posts_content(item, post_locator)

    @step("Validate posts content")
    def validate_posts_content(self, data, post_locator):
        with pulse_step("Get posts content from API Response"):
            if data.get("text") and data["text"].strip():
                body_locator = post_locator.locator(LatestPostsLocators.POSTS_BODY)
                self.base_page.verify_element_text(body_locator, data["text"].strip())

        with pulse_step("Validate posts images"):
            if data.get("photoIds"):
                for index, photo_id in enumerate(data["photoIds"]):
                    image_locator = post_locator.locator(
                        LatestPostsLocators.POSTS_IMAGE
                    ).nth(index)
                    self.base_page.verify_attribute_value_contains(
                        image_locator, "src", str(photo_id)
                    )
