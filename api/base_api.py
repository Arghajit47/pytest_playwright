class BaseAPI:
    def __init__(self, page):
        self.page = page

    def get_response(self, request_setup, url, headers=None, queryParams=None):
        response = request_setup.get(url, headers=headers, params=queryParams)
        if response.status != 200:
            print(f"GET Failed: {response.status} - {response.text()}")
        assert response.status == 200
        return response.json()

    def post_response(self, request_setup, url, headers=None, data=None):
        response = request_setup.post(url, headers=headers, data=data)
        if response.status not in [200, 201]:
            print(f"POST Failed: {response.status} - {response.text()}")
        assert response.status in [200, 201]
        return response.json()

    def delete_response(self, request_setup, url, headers=None):
        response = request_setup.delete(url, headers=headers)
        if response.status not in [200, 202, 204]:
            print(f"DELETE Failed: {response.status} - {response.text()}")
        assert response.status in [200, 202, 204]
        try:
            return response.json()
        except:
            return {}

    def put_response(self, request_setup, url, headers=None, data=None):
        response = request_setup.put(url, headers=headers, data=data)
        if response.status not in [200, 201, 204]:
            print(f"PUT Failed: {response.status} - {response.text()}")
        assert response.status in [200, 201, 204]
        return response.json()

    def patch_response(self, request_setup, url, headers=None, data=None):
        response = request_setup.patch(url, headers=headers, data=data)
        if response.status not in [200, 201]:
            print(f"PATCH Failed: {response.status} - {response.text()}")
        assert response.status in [200, 201]
        return response.json()
