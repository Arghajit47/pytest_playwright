from constants.components.dashboard.latest_posts_locators import LatestPostsConstants


class LatestPostsLocators:
    HEADER = f".orangehrm-dashboard-widget-header:has-text('{LatestPostsConstants.LATEST_POSTS_WIDGET_TEXT}') p"
    POSTS_CONTAINER = "div.orangehrm-buzz-widget-card"
    POSTS_IMAGE = "img.orangehrm-buzz-widget-picture"
    POSTS_USER_IMAGE = "div.orangehrm-buzz-profile-image img[alt='profile picture']"
    POSTS_USER_NAME = "p.orangehrm-buzz-widget-header-emp"
    POSTS_CREATION_TIME = "p.orangehrm-buzz-widget-header-time"
    POSTS_BODY = "p.orangehrm-buzz-widget-body"
