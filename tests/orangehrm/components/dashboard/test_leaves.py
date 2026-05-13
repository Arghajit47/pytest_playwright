import pytest
from pages.components.dashboard.leaves_components import LeavesComponent


@pytest.mark.usefixtures("login", "logout")
class TestLeaves:

    @pytest.mark.pulse_severity("Medium")
    @pytest.mark.pulse_tag("Regression")
    @pytest.mark.pulse_tag("AboutMe")
    def test_about_me_ui_api_validation(self, page, request_setup, login_via_api):
        leaves_component = LeavesComponent(page)
        leaves_component.verify_leaves_widget_text()
        leaves_component.validate_no_content_in_leaves_widget(
            request_setup, login_via_api
        )
