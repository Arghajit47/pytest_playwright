from constants.components.dashboard.subunits_constants import SubunitsPageConstants

class SubnitLocators:
    SUBUNIT_WIDGET_TEXT = f".orangehrm-dashboard-widget:has-text('{SubunitsPageConstants.SUBUNIT_WIDGET_TEXT}') p"
    SUBUNIT_LEGENDS = lambda subunit_name: (
        f".orangehrm-dashboard-widget:has-text('{SubunitsPageConstants.SUBUNIT_WIDGET_TEXT}') span[title='{subunit_name}']"
    )
    SUBUNIT_PIE_CHART = f".orangehrm-dashboard-widget:has-text('{SubunitsPageConstants.SUBUNIT_WIDGET_TEXT}') canvas"
