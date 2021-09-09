from oauth_micro_client import oauth_client


def test_get_resource():
    with oauth_client.open() as client:
        error, response = client.get_resource(
            "cd2a6213-e7ce-4682-a3db-73e745e57f86")
