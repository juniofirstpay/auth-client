import pytest

from oauth_micro_client import OAuthClient

class TestOauth:
    oauth_client = OAuthClient()

    def test_introspection(self):
        auth_token = "BO0N33mx9YaxmsJo9NIabChaHjd8wOMiOvOY3rSQJG"

        with self.oauth_client.open() as client:
            error, response = client.introspection(auth_token)
            assert not error
            assert response.get('username') is not None
            print(response.get('username'))

    def test_create_user(self):
        data_dict = {
            "token": "1999000117",
            "token_type": 1,
            "auth_key": "1111",
            "username": "F201C3C3-888F-4073-27AB-08D8EEE68536",
            "device_id": "abcd"
        }

        with self.oauth_client.open() as client:
            error, response = client.create_user(**data_dict)
            assert not error
            assert response.get('error') is not None
            print(response.get('error'))

    def test_get_user(self):
        auth_token = "BO0N33mx9YaxmsJo9NIabChaHjd8wOMiOvOY3rSQJG"

        with self.oauth_client.open() as client:
            error, response = client.get_user(auth_token=auth_token)
            assert not error
            assert response.get('username') is not None
            print(response.get('username'))

    def test_generate_token(self):
        data_dict = {
            "token": "1999000116",
            "token_type": 1,
            "auth_key": "1111"
        }

        with self.oauth_client.open() as client:
            error, response = client.generate_token(**data_dict)
            assert not error
            assert response.get('access_token') is not None
            print(response.get('access_token'))

    def test_update_user(self):
        data_dict = {
            "token": "1999000117",
            "token_type": 1,
            "auth_key": "1111",
            "username": "F201C3C3-888F-4073-27AB-08D8EEE68536",
            "device_id": "abcd",
            "person_id": "person1"
        }

        with self.oauth_client.open() as client:
            error, response = client.update_user(**data_dict)
            assert not error
            assert response.get('access_token') is not None
            print(response.get('access_token'))

    def test_find_user_by_token(self):
        data_dict = {
            "token": "1999000117",
            "token_type": 1,
        }

        with self.oauth_client.open() as client:
            error, response = client.find_user_by_token(**data_dict)
            assert not error
            assert response.get('username') is not None
            print(response.get('username'))

    def test_find_user_by_person_id(self):
        data_dict = {
            "person_id": "person1"
        }

        with self.oauth_client.open() as client:
            error, response = client.find_user_by_person_id(**data_dict)
            assert not error
            assert response.get('username') is not None
            print(response.get('username'))

    def test_check_user(self):
        data_dict = {
            "token": "1999000117",
            "token_type": 1,
            "device_id": "abcd"
        }

        with self.oauth_client.open() as client:
            error, response = client.check_user(**data_dict)
            assert not error
            assert response.get('code') is not None
            print(response.get('code'))

    def test_generate_otp(self):
        data_dict = {
            "mobile_num": "1999000117",
            "action": "generate"
        }

        with self.oauth_client.open() as client:
            error, response = client.generate_otp(**data_dict)
            assert not error
            assert response.get('token') is not None
            print(response.get('token'))

    def test_verify_otp(self):
        data_dict = {
            "mobile_num": "1999000117",
            "token": "719356013a43023d17eee1115be5429f",
            "otp": "5699",
            "action": "validate"
        }

        with self.oauth_client.open() as client:
            error, response = client.verify_otp(**data_dict)
            assert error
            assert response.get('Success') is not None
            print(response.get('Success'))
