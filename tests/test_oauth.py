import pytest
from oauth_micro_client import oauth_client

class TestOauth:

    def test_introspection(self):
        token = "BO0N33mx9YaxmsJo9NIabChaHjd8wOMiOvOY3rSQJG"
        with oauth_client.open() as client:
            error, response = client.introspection(token)
            assert not error
            assert response.get('username') is not None
            print(response.get('username'))