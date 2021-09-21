import pytest
import random
import string
from oauth_micro_client import OAuthClient


class StorageClass:

    otp_token = None
    username = None
    user_access_token = None
    username = None
    _mobile_number = None
    _mobile_number2 = None

    client_access_token = None

    @property
    def mobile_number(self):
        if self._mobile_number:
            return self._mobile_number
        self._mobile_number = "18" + \
            "".join(random.choices(string.digits, k=8))
        return self._mobile_number

    @property
    def mobile_number2(self):
        if self._mobile_number2:
            return self._mobile_number2
        self._mobile_number2 = "18" + \
            "".join(random.choices(string.digits, k=8))
        return self._mobile_number2


class TestOauth:
    oauth_client = OAuthClient()
    storage = StorageClass()

    client_id = "AR0mZLSxDLvALHfv"
    client_secret = "reYAnAKzEjqiUGAhvqiyYWqejSspoHTj5geVYbDoeSrpReDUv9M8VTd5YU6xcL9R"

    def test_generate_otp(self):
        with self.oauth_client.open() as client:
            error, response = client.generate_otp(
                self.client_id,
                self.client_secret,
                self.storage.mobile_number
            )
            assert error is None
            assert response.get('otp_token') is not None
            self.storage.otp_token = response.get('otp_token')

    def test_verify_otp(self):
        with self.oauth_client.open() as client:
            error, response = client.verify_otp(
                self.client_id,
                self.client_secret,
                self.storage.mobile_number,
                self.storage.otp_token,
                "9090"
            )
            assert error is None
            assert response.get('success') == True

    def test_user_registration(self):
        with self.oauth_client.open() as client:
            error, response = client.register(
                self.client_id,
                self.client_secret,
                "device_123",
                self.storage.mobile_number,
                "1",
                "1234",
                "9090",
                self.storage.otp_token,
            )
            assert error is None
            assert response.get('username') is not None
            self.storage.username = response.get("username")

    def test_access_token(self):
        with self.oauth_client.open() as client:
            error, response = client.authorize(
                self.client_id,
                self.client_secret,
                "password",
                "profile",
                self.storage.mobile_number,
                "1",
                "1234",
            )
            assert error is None
            assert response.get('access_token') is not None
            self.storage.user_access_token = response.get("access_token")

    def test_user_profile(self):
        with self.oauth_client.open() as client:
            error, response = client.get_user(self.storage.user_access_token)
            assert error is None
            assert response.get("username") == self.storage.username

    def test_client_create_user(self):
        with self.oauth_client.open() as client:
            error, response = client.create_user(
                self.storage.mobile_number2,
                "1",
                None,
                None,
                "device_3"
            )
            assert error is None
            assert isinstance(response, dict)
            assert response.get("username") is not None

    def test_client_get_user(self):
        with self.oauth_client.open() as client:
            error, response = client.get_user(self.storage.user_access_token)
            assert error is None
            assert isinstance(response, dict)
            assert response.get("username") is not None

    def test_check_user(self):
        with self.oauth_client.open() as client:
            error, response = client.check_user(
                self.storage.mobile_number2,
                "device_3"
            )
            assert error is None
            assert isinstance(response, dict)
            assert response.get('message') in ('Ok', 'Not Exist')

    # def test_introspection(self):
    #     auth_token = "BO0N33mx9YaxmsJo9NIabChaHjd8wOMiOvOY3rSQJG"

    #     with self.oauth_client.open() as client:
    #         error, response = client.introspection(auth_token)
    #         assert not error
    #         assert response.get('username') is not None
    #         print(response.get('username'))

    # def test_create_user(self):
    #     data_dict = {
    #         "token": "1999000117",
    #         "token_type": 1,
    #         "auth_key": "1111",
    #         "username": "F201C3C3-888F-4073-27AB-08D8EEE68536",
    #         "device_id": "abcd"
    #     }

    #     with self.oauth_client.open() as client:
    #         error, response = client.create_user(**data_dict)
    #         assert not error
    #         assert response.get('error') is not None
    #         print(response.get('error'))

    # def test_get_user(self):
    #     auth_token = "BO0N33mx9YaxmsJo9NIabChaHjd8wOMiOvOY3rSQJG"

    #     with self.oauth_client.open() as client:
    #         error, response = client.get_user(auth_token=auth_token)
    #         assert not error
    #         assert response.get('username') is not None
    #         print(response.get('username'))

    # def test_generate_token(self):
    #     data_dict = {
    #         "token": "1999000116",
    #         "token_type": 1,
    #         "auth_key": "1111"
    #     }

    #     with self.oauth_client.open() as client:
    #         error, response = client.generate_token(**data_dict)
    #         assert not error
    #         assert response.get('access_token') is not None
    #         print(response.get('access_token'))

    # def test_update_user(self):
    #     data_dict = {
    #         "token": "1999000117",
    #         "token_type": 1,
    #         "auth_key": "1111",
    #         "username": "F201C3C3-888F-4073-27AB-08D8EEE68536",
    #         "device_id": "abcd",
    #         "person_id": "person1"
    #     }

    #     with self.oauth_client.open() as client:
    #         error, response = client.update_user(**data_dict)
    #         assert not error
    #         assert response.get('access_token') is not None
    #         print(response.get('access_token'))

    # def test_find_user_by_token(self):
    #     data_dict = {
    #         "token": "1999000117",
    #         "token_type": 1,
    #     }

    #     with self.oauth_client.open() as client:
    #         error, response = client.find_user_by_token(**data_dict)
    #         assert not error
    #         assert response.get('username') is not None
    #         print(response.get('username'))

    # def test_find_user_by_person_id(self):
    #     data_dict = {
    #         "person_id": "person1"
    #     }

    #     with self.oauth_client.open() as client:
    #         error, response = client.find_user_by_person_id(**data_dict)
    #         assert not error
    #         assert response.get('username') is not None
    #         print(response.get('username'))

    # def test_check_user(self):
    #     data_dict = {
    #         "token": "1999000117",
    #         "token_type": 1,
    #         "device_id": "abcd"
    #     }

    #     with self.oauth_client.open() as client:
    #         error, response = client.check_user(**data_dict)
    #         assert not error
    #         assert response.get('code') is not None
    #         print(response.get('code'))

    # def test_generate_otp(self):
    #     data_dict = {
    #         "mobile_num": "1999000117",
    #         "action": "generate"
    #     }

    #     with self.oauth_client.open() as client:
    #         error, response = client.generate_otp(**data_dict)
    #         assert not error
    #         assert response.get('token') is not None
    #         print(response.get('token'))

    # def test_verify_otp(self):
    #     data_dict = {
    #         "mobile_num": "1999000117",
    #         "token": "719356013a43023d17eee1115be5429f",
    #         "otp": "5699",
    #         "action": "validate"
    #     }

    #     with self.oauth_client.open() as client:
    #         error, response = client.verify_otp(**data_dict)
    #         assert error
    #         assert response.get('Success') is not None
    #         print(response.get('Success'))
