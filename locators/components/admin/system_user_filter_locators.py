class SystemUserFilterLocators:
    ADMIN_OPTION = "//a[contains(@href, 'viewAdminModule')]/child::span"
    USER_LIST_COUNT = (
        "div[class='orangehrm-horizontal-padding orangehrm-vertical-padding'] span"
    )
    USER_LIST_ROWS = "//div[@class='oxd-table-body']//div[@role='row']"
    USER_LIST_CELLS = lambda row, col: (
        f"(//div[@class='oxd-table-body']//div[@role='row'])[{row}]//div[@role='cell'][{col}]/div"
    )
