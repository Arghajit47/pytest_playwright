class AboutMeLocators:
    ABOUT_ME_BUTTON = '//a[@class="oxd-userdropdown-link"][contains(@href, "#")]'
    ABOUT_ME_MODAL = "div[role='document']"
    ABOUT_ME_MODAL_HEADER = "div[role='document'] h6"
    ABOUT_ME_MODAL_KEY_FIELDS = "div[role='document'] p.orangehrm-about-title"
    ABOUT_ME_MODAL_VALUE_FIELDS = "div[role='document'] p.orangehrm-about-text"
    ABOUT_ME_MODAL_CLOSE_BTN = (
        "div[role='document'] button.oxd-dialog-close-button-position"
    )
