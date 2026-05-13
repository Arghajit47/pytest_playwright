import pytest
from pages.about_me import AboutMePage


@pytest.mark.usefixtures("login", "logout")
class TestAboutMe:

    @pytest.mark.pulse_severity("Medium")
    @pytest.mark.pulse_tag("Regression")
    @pytest.mark.pulse_tag("AboutMe")
    def test_about_me_ui_api_validation(self, page, request_setup, login_via_api):
        """
        Test to verify that the 'About Me' modal details in the UI match the data from the API.
        This test uses a hybrid UI-API approach for validation.
        """
        about_me_page = AboutMePage(page)
        
        # 1. Trigger the 'About' modal from the user avatar dropdown
        about_me_page.click_on_user_avatar()
        
        # 2. Perform the UI-API hybrid validation
        about_me_page.verify_about_me_modal_details(request_setup, login_via_api)

        # 3. Close the modal to ensure clean state for logout
        about_me_page.close_about_me_modal()
