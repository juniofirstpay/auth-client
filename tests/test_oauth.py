import pytest
from oauth_micro_client import oauth_client

class TestOauth:

    def test_introspection(self):
        auth_token = "BO0N33mx9YaxmsJo9NIabChaHjd8wOMiOvOY3rSQJG"

        with oauth_client.open() as client:
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

        with oauth_client.open() as client:
            error, response = client.create_user(**data_dict)
            assert not error
            assert response.get('error') is not None
            print(response.get('error'))

    def test_get_user(self):
        auth_token = "BO0N33mx9YaxmsJo9NIabChaHjd8wOMiOvOY3rSQJG"

        with oauth_client.open() as client:
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

        with oauth_client.open() as client:
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

        with oauth_client.open() as client:
            error, response = client.update_user(**data_dict)
            assert not error
            assert response.get('access_token') is not None
            print(response.get('access_token'))
