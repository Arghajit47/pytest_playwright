import pytest

from pages.components.dashboard.latest_posts_components import LatestPostsComponent
from pytest_pulse import pulse_step

pytestmark = pytest.mark.usefixtures(
    "login_via_api", "login_via_cookies", "request_setup"
)


@pytest.mark.pulse_severity("Minor")
@pytest.mark.pulse_tag("Regression")
@pytest.mark.pulse_tag("Dashboard")
@pytest.mark.pulse_tag("Latest Posts")
def test_latest_posts_component(page, request_setup, login_via_api):
    with pulse_step("Instantiate Latest Posts Component"):
        latest_posts_component = LatestPostsComponent(page)
    with pulse_step("Check if Latest Posts widget is visible"):
        if not latest_posts_component.is_widget_visible():
            pytest.skip("Buzz Latest Posts widget is not visible (module likely disabled)")
    with pulse_step("Verify Latest Posts widget text"):
        latest_posts_component.verify_latest_posts_widget_text()
    with pulse_step("Get Latest Posts Items from API"):
        response = latest_posts_component.get_latest_posts_data(
            request_setup, login_via_api
        )
    print(f"API Response: {response}")
    with pulse_step("Validate Latest Posts Items"):
        latest_posts_component.validate_latest_posts_data(response)
