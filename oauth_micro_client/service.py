import requests
from urllib.parse import urljoin
from typing import List, Dict, Tuple, Optional

from requests.models import Response


class OAuthService(object):

    base_url_introspect = '/oauth/introspect'

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

    def introspection(self, token: str):
        data = {
            "authorization": token
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
