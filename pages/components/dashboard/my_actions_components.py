import re
from constants.api_constants import APIEndpoints
from constants.components.dashboard.my_actions_constants import MyActionsPageConstants
from locators.components.dashboard.my_actions_locators import MyActionsLocators
from pages.base_page import BasePage


class MyActionsComponent:

    def __init__(self, page, pulse_step):
        self.page = page
        self.base_page = BasePage(page, pulse_step)

    def verify_my_actions_widget_text(self):
        self.base_page.verify_element_text(
            MyActionsLocators.MY_ACTIONS_WIDGET_TEXT,
            MyActionsPageConstants.MY_ACTIONS_WIDGET_TEXT,
        )

    def get_my_action_items_from_api(self, request_setup, login_via_api):
        response = request_setup.get(
            APIEndpoints.ACTION_ITEMS_ENDPOINT,
            headers={"Cookie": f"orangehrm={login_via_api}"},
        )
        assert response.status == 200
        return response.json()

    def singularize(self, data):
        if data["pendingActionCount"] == 1:
            return re.sub(r"s(\s|$)", r"\1", data["group"])
        else:
            return data["group"]

    def validate_my_action_items(self, response):
        if response["data"] == []:
            print("No items in my action items")
        else:
            print("Items in my action items found!")
            for i in range(len(response["data"])):
                print(response["data"][i])
                self.base_page.verify_element_text_ignore_case(
                    MyActionsLocators.MY_ACTION_LIST_ITEMS,
                    f"({response['data'][i]['pendingActionCount']}) {self.singularize(response['data'][i])}",
                    i,
                )
