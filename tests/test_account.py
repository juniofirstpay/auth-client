import pytest
from oauth_micro_client import oauth_client
from datetime import datetime

class TestCreateAccountHolder:

    def test_create_account(self):
        account_holder_id = '3ae7912c-013e-4c98-b004-a9c416285126'
        account_name = "ac://test4"
        with oauth_client.open() as client:
            (error, response) = client.create_account(account_holder_id, account_name)
            print(error, response)
            assert response.get('oauth_ref_id') is not None
            # response = client.get_account_holder("id", response.get('individual_id'))
            # assert response.get('individual_id') == '3ae7912c-013e-4c98-b004-a9c416285126'

    def test_get_account(self):
        account_id = "ed5bedb7-9ac5-448e-9e6c-6f4c7f5eb149"
        with oauth_client.open() as client:
            (error, response) = client.get_account(account_id)
            assert error is None
            assert isinstance(response, dict)
            assert response.get('oauth_ref_id') == "ed5bedb7-9ac5-448e-9e6c-6f4c7f5eb149"


    def test_get_accounts(self):
        account_holder_id = "3ae7912c-013e-4c98-b004-a9c416285126"
        with oauth_client.open() as client:
            (error, response) = client.get_accounts(account_holder_id)
            print(error, response)
            assert error is None
            assert isinstance(response, list)
            # assert response.get('oauth_ref_id') == "ed5bedb7-9ac5-448e-9e6c-6f4c7f5eb149"
    
    def test_block_account(self):
        account_id = ""
        status = "BLOCKED"
        with oauth_client.open() as client:
            (error, response) = client.update_account(account_id, status)
            print(error, response)
            assert error is None
            assert isinstance(response, dict)
            assert response.get("status") == status

    # def test_enable_account(self):
    #     account_id = "ed5bedb7-9ac5-448e-9e6c-6f4c7f5eb149"
    #     status = "ENABLED"
    #     with oauth_client.open() as client:
    #         (error, response) = client.update_account(account_id, status)
    #         print(error, response)
    #         assert error is None
    #         assert isinstance(response, dict)
    #         assert response.get("status") == status

    # def test_close_account(self):
    #     account_id = "ed5bedb7-9ac5-448e-9e6c-6f4c7f5eb149"
    #     status = "CLOSED"
    #     with oauth_client.open() as client:
    #         (error, response) = client.close_account(account_id)
    #         print(error, response)
    #         assert error is None
    #         assert isinstance(response, dict)
    #         assert response.get("status") == status

    # def test_get_account_holder(self):
    #     with oauth_client.open() as client:
    #         response = client.get_account_holder("id", '3ae7912c-013e-4c98-b004-a9c416285126')
    #         assert response.get('individual_id') == '3ae7912c-013e-4c98-b004-a9c416285126'
    