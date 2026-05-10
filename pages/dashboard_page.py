from constants.common_constants import Attributes
from locators.dashboard_locators import DashboardLocators
from pages.base_page import BasePage
from constants.dashboard_page_constants import DashboardPageConstants


class DashboardPage:

    def __init__(self, page, pulse_step):
        self.page = page
        self.base_page = BasePage(page, pulse_step)

    def verify_dashboard_page_url_title(self):
        self.base_page.verify_page_url(DashboardPageConstants.DASHBOARD_PAGE_URL)
        self.base_page.verify_page_title(DashboardPageConstants.DASHBOARD_PAGE_TITLE)

    def verify_dashboard_page_header(self):
        self.base_page.verify_element_text(
            DashboardLocators.PAGE_HEADER,
            DashboardPageConstants.DASHBOARD_PAGE_HEADER,
        )

    def verify_upgrade_button_is_visible(self):
        self.base_page.verify_element_is_visible(DashboardLocators.UPGRADE_BUTTON)
        self.base_page.verify_element_text(
            DashboardLocators.UPGRADE_BUTTON,
            DashboardPageConstants.UPGRADE_BTN_TEXT,
        )

    def verify_dashboard_widgets_count(self):
        self.base_page.verify_element_count(
            DashboardLocators.DASHBOARD_WIDGETS,
            DashboardPageConstants.DASHBOARD_WIDGETS_COUNT,
        )

    def verify_dashboard_widgets_texts(self):
        self.base_page.verify_all_element_texts(
            DashboardLocators.DASHBOARD_WIDGETS_TITLE,
            DashboardPageConstants.DASHBOARD_WIDGETS_TITLES,
        )

    def verify_profile_image_src(self):
        dropdown_src = self.base_page.get_attribute(
            DashboardLocators.DASHBOARD_PROFILE_DROPDOWN_IMAGE,
            Attributes.SRC.value,
        )
        time_at_work_src = self.base_page.get_attribute(
            DashboardLocators.TIME_AT_WORK_USER_IMAGE,
            Attributes.SRC.value,
        )

        # Remove domain and query parameters to compare only the path
        # e.g., converts "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPhoto/empNumber/7" to "/viewPhoto/empNumber/7"
        path1 = dropdown_src.split("?")[0].split("pim")[-1]
        path2 = time_at_work_src.split("?")[0].split("pim")[-1]

        self.base_page.verify_equal(path1, path2)

    def capture_dashboard_screenshot_and_attach_to_report(
        self, pulse_attach, path: str = "screenshots"
    ):
        self.base_page.capture_screenshot(path + "/dashboard_screenshot.png")
        pulse_attach("screenshots/dashboard_screenshot.png")
