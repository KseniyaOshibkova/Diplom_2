import requests
from api.url import Urls

class ApiClient:
    def __init__(self, base_url=Urls.BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, path, **kwargs):
        return self.session.get(self.base_url + path, **kwargs)

    def post(self, path, **kwargs):
        return self.session.post(self.base_url + path, **kwargs)

    def delete(self, path, **kwargs):
        return self.session.delete(self.base_url + path, **kwargs)

    def patch(self, path, **kwargs):
        return self.session.patch(self.base_url + path, **kwargs)
