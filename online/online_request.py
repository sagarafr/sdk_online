import requests


class OnlineRequest:
    def __init__(self, token: str=None):
        self._url_base = "https://api.online.net/api/v1"
        self._auth = {'Authorization': "Bearer " + token}

    @property
    def url_base(self):
        return self._url_base

    @property
    def auth(self):
        return self._auth

    def get(self, url: str):
        r = requests.get(self.url_base + url, headers=self.auth)
        return r.json()

    def post(self, url, **kwargs):
        r = requests.post(self.url_base + url, data=kwargs, header=self.auth)
        return r.json()

    def delete(self, url, **kwargs):
        r = requests.post(self.url_base + url, data=kwargs, header=self.auth)
        return r.json()
