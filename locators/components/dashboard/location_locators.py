from constants.components.dashboard.locations_constants import LocationsPageConstants


class LocationsPageLocators:
    LOCATIONS_WIDGET_TEXT = f".orangehrm-dashboard-widget:has-text('{LocationsPageConstants.LOCATIONS_WIDGET_TEXT}') p"
    LOCATIONS_LEGENDS = lambda location_name: (
        f".orangehrm-dashboard-widget:has-text('{LocationsPageConstants.LOCATIONS_WIDGET_TEXT}') span[title='{location_name}']"
    )
    LOCATIONS_PIE_CHART = f".orangehrm-dashboard-widget:has-text('{LocationsPageConstants.LOCATIONS_WIDGET_TEXT}') canvas"
