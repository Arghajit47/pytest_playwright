class APIEndpoints:
    USERS_ENDPOINT = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/admin/users?limit=50&offset=0&sortField=u.userName&sortOrder=ASC"
    BASE_URL = "https://opensource-demo.orangehrmlive.com"
    USER_NAME = "Admin"
    PASSWORD = "admin123"
    ACTION_ITEMS_ENDPOINT = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/dashboard/employees/action-summary"
    SHORTCUTS_ENDPOINT = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/dashboard/shortcuts"
    DUMMYJSON_AUTHENTICATION_ENDPOINT = "https://dummyjson.com/auth/me"
    DUMMYJSON_LOGIN_ENDPOINT = "https://dummyjson.com/auth/login"
    ABOUT_ME_API_ENDPOINT = (
        "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/core/about"
    )
    DASHBOARD_LEAVES_ENDPOINT = lambda date: f"https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/dashboard/employees/leaves?date={date}"
    DASHBOARD_EMPLOYEE_SUBUNIT = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/dashboard/employees/subunit"
    DASHBOARD_EMPLOYEE_BY_LOCATION = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/dashboard/employees/locations"
    DASHBOARD_LATEST_POSTS = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/buzz/feed?limit=5&offset=0&sortOrder=DESC&sortField=share.createdAtUtc"
