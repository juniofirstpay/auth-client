import requests
from urllib.parse import urljoin
from typing import List, Dict, Tuple, Optional

from requests.models import Response


class OAuthService(object):

    base_url_introspect = 'oauth/introspect'
    base_url_create_user = 'api/user/create'
    base_url_get_user = 'api/user/info'
    base_url_generate_token = 'oauth/token'
    base_url_update_user = 'api/user/update'
    base_url_find_user = 'api/user/find'
    base_url_check_user = 'api/user/check'
    base_url_otp = 'oauth/otp'
    base_url_verify_otp = 'oauth/otp'
    base_url_register = 'api/user/register'
    base_url_access_verify = 'api/otp/access'

    def __init__(self, endpoint: str, client_id: str, client_secret: str, api_key):
        self.base_url = endpoint
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_headers = {
            "Authorization": f"Bearer {api_key}"
        }

    def open(self):
        self.request = requests.Session()
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

    def authorize(self, *args, **kwargs):
        response = self.request.post(
            url=urljoin(self.base_url,
                        self.base_url_generate_token),
            json=kwargs
        )
        return self.process_response(response)
       
    def authorize_via_otp(self, *args, **kwargs):
        response = self.request.post(
            url=urljoin(self.base_url,
                        self.base_url_generate_token),
            json=kwargs
        )
        return self.process_response(response)

    def register(self, *args, **kwargs):
        response = self.request.post(
            url=urljoin(self.base_url,
                        self.base_url_register),
            json=kwargs
        )
        return self.process_response(response)

    def otp(self, *args, **kwargs):
        response = self.request.post(
            url=urljoin(self.base_url,
                        self.base_url_otp),
            json=kwargs
        )
        return self.process_response(response)

    def validate_access(self, *args , **kwargs):
        response = self.request.post(
            url=urljoin(self.base_url,
                        self.base_url_access_verify),
            json=kwargs
        )
        return self.process_response(response)

    def introspection(self, *args, **kwargs):

        response = self.request.post(
            url=urljoin(
                self.base_url,
                self.base_url_introspect
            ),
            json={**kwargs, "client_id": self.client_id,
                  "client_secret": self.client_secret}
        )
        return self.process_response(response)

    def create_user(
        self,
        token: str,
        token_type: int,
        username: Optional[str] = None,
        auth_key: Optional[str] = None,
        device_id: Optional[str] = None,
        migration_status: Optional[int] = 2
    ):
        data = {
            "token": token,
            "token_type": token_type
        }
        if username:
            data["username"] = username
        if auth_key:
            data["auth_key"] = auth_key
        if device_id:
            data["device_id"] = device_id

        if migration_status:
            data["migration_status"] = migration_status

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
        headers = {}
        headers.update({"Authorization": f'Bearer {auth_token}'})
        response = self.request.get(
            url=urljoin(
                self.base_url,
                self.base_url_get_user
            ),
            headers=headers,
        )
        return self.process_response(response)

    def generate_token(
        self,
        token: str,
        token_type: str,
        auth_key: str
    ):
        data = {
            "token": token,
            "token_type": token_type,
            "auth_key": auth_key,
        }
        headers = self.base_headers
        response = self.request.post(
            url=urljoin(
                self.base_url,
                self.base_url_generate_token
            ),
            headers=self.base_headers,
            json=data
        )
        return self.process_response(response)

    def update_user(
        self,
        token: str,
        token_type: int,
        username: str,
        auth_key: Optional[str],
        device_id: Optional[str],
        person_id: Optional[str],
    ):
        data = {
            "token": token,
            "token_type": token_type,
            "auth_key": auth_key,
            "username": username,
            "person_id": person_id,
            "device_id": device_id,
        }
        headers = self.base_headers
        response = self.request.post(
            url=urljoin(
                self.base_url,
                self.base_url_update_user
            ),
            headers=self.base_headers,
            json=data
        )
        return self.process_response(response)

    # def find_user_by_token(
    #     self,
    #     token: str,
    #     token_type: int,
    #     username: str,
    #     auth_key: Optional[str],
    #     device_id: Optional[str],
    #     person_id: Optional[str],
    # ):
    #     data = {
    #         "token": token,
    #         "token_type": token_type,
    #         "auth_key": auth_key,
    #         "username": username,
    #         "person_id": person_id,
    #         "device_id": device_id,
    #     }
    #     headers = self.base_headers
    #     response = self.request.post(
    #         url=urljoin(
    #             self.base_url,
    #             self.base_url_update_user
    #         ),
    #         headers=self.base_headers,
    #         json=data
    #     )
    #     return self.process_response(response)

    def find_user_by_token(
        self,
        token: str,
        token_type: int
    ):
        data = {
            "value": token,
            "type": token_type
        }
        headers = self.base_headers
        response = self.request.post(
            url=urljoin(
                self.base_url,
                self.base_url_find_user
            ),
            headers=self.base_headers,
            json=data
        )
        return self.process_response(response)

    def find_user_by_person_id(
        self,
        person_id: str
    ):
        data = {
            "person_id": person_id,
        }
        headers = self.base_headers
        response = self.request.post(
            url=urljoin(
                self.base_url,
                self.base_url_find_user
            ),
            headers=self.base_headers,
            json=data
        )
        return self.process_response(response)

    def check_user(
        self,
        token: str,
        device_id: str
    ):
        data = {
            "token": token,
            "device_id": device_id,
        }
        response = self.request.post(
            url=urljoin(
                self.base_url,
                self.base_url_check_user
            ),
            headers=self.base_headers,
            json=data
        )
        return self.process_response(response)

    def generate_otp(
        self,
        mobile_num: str,
        action: str,
        scope : str = None
    ):
        data = {
            "mobile_num": mobile_num,
            "action": action, 
            "scope" : scope
        }
        headers = self.base_headers
        response = self.request.post(
            url=urljoin(
                self.base_url,
                self.base_url_generate_otp
            ),
            headers=self.base_headers,
            json=data
        )
        return self.process_response(response)

    def verify_otp(
        self,
        mobile_num: str,
        action: str,
        token: str,
        otp: str,
        scope: str = None
    ):
        data = {
            "mobile_num": mobile_num,
            "action": action,
            "token": token,
            "otp": otp,
            "scope" : scope
        }
        headers = self.base_headers
        response = self.request.post(
            url=urljoin(
                self.base_url,
                self.base_url_verify_otp
            ),
            headers=self.base_headers,
            json=data
        )
        return self.process_response(response)

    def add_user(
        self,
        **kwargs
    ):
        headers = self.base_headers
        self.request.post(
            url=urljoin(self.base_url, self.base_url_add_user),
            headers=self.base_headers,
            json=data
        )
