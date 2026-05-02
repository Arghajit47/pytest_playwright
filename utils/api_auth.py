import requests
import re

class OrangeHRMAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        # Standard headers to mimic a real browser
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json, text/plain, */*'
        })

    def login(self, username, password):
        # 1. Get the login page to grab the initial cookie and CSRF token
        login_page_url = f"{self.base_url}/web/index.php/auth/login"
        response = self.session.get(login_page_url)
        
        # Extract the CSRF token from the page source
        # OrangeHRM stores it in a Vue component attribute: :token="&quot;TOKEN_VALUE&quot;"
        token_match = re.search(r':token="&quot;([^&]+)&quot;"', response.text)
        if not token_match:
            raise Exception("Could not find CSRF token on login page.")
        
        csrf_token = token_match.group(1)
        
        # 2. Submit the credentials to the validate endpoint
        login_data = {
            '_token': csrf_token,
            'username': username,
            'password': password
        }
        
        validate_url = f"{self.base_url}/web/index.php/auth/validate"
        login_response = self.session.post(validate_url, data=login_data)
        
        # If successful, OrangeHRM redirects (302) to the dashboard. 
        # requests.Session automatically updates the 'orangehrm' cookie here.
        if login_response.status_code == 200:
            print("Successfully authenticated!")
            return self.session.cookies.get_dict().get('orangehrm')
        else:
            print(f"Login failed with status: {login_response.status_code}")
            return None
