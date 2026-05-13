from enum import Enum


class AboutMeKeys(Enum):
    COMPANY_NAME = "Company Name:"
    VERSION = "Version:"
    ACTIVE_EMPLOYEES = "Active Employees:"
    EMPLOYEES_TERMINATED = "Employees Terminated:"


ABOUT_ME_MODAL_HEADER_TEXT = "About"


class AboutMeAPIResponseKeys(Enum):
    COMPANY_NAME = "companyName"
    PRODUCT_NAME = "productName"
    VERSION = "version"
    ACTIVE_EMPLOYEES = "numberOfActiveEmployee"
    EMPLOYEES_TERMINATED = "numberOfPastEmployee"
