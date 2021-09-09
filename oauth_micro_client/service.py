import requests
from urllib.parse import urljoin
from typing import List, Dict, Tuple, Optional

from requests.models import Response


class OAuthService(object):

    base_url_introspect = '/oauth/introspect'

    base_url_create_user = '/api/user/create'

    base_url_get_user = '/api/user/info'

    def __init__(self, endpoint: str, client_id: str, client_secret: str):
        self.base_url = endpoint
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_headers = {
            'Client': self.client_id,
            'Secret': self.client_secret,
        }

    def open(self):
        self.request = requests.Session()
        self.request.headers.update(self.base_headers)
        return self

    def close(self):
        self.request.close()
        self.request = None

    def process_response(sef, response: Response):
        if response.status_code == 200:
            return (None, response.json())
        else:
            try:
                return (response.status_code, response.json())
            except:
                return (response.status_code, response.text)

    def introspection(self, auth_token: str):
        data = {
            "authorization": auth_token
        }
        response = self.request.post(
            url=urljoin(
                self.base_url,
                self.base_url_introspect
            ),
            headers=self.base_headers,
            json=data
        )
        return self.process_response(response)

    def create_user(
        self,
        token: str,
        token_type: int,
        username: str,
        auth_key: Optional[str],
        device_id: Optional[str]
    ):
        data = {
            "token": token,
            "token_type": token_type,
            "auth_key": auth_key,
            "username": username,
            "device_id": device_id,
        }
        response = self.request.post(
            url=urljoin(
                self.base_url,
                self.base_url_create_user
            ),
            headers=self.base_headers,
            json=data
        )
        return self.process_response(response)

    def get_user(
        self,
        auth_token: str
    ):
        headers = self.base_headers
        headers.update({"Authorization": f'Bearer {auth_token}'})
        response = self.request.get(
            url=urljoin(
                self.base_url,
                self.base_url_get_user
            ),
            headers=self.base_headers,
        )
        return self.process_response(response)
