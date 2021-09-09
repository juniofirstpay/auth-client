from typing import ContextManager, Dict, List, Tuple, Optional
from contextlib import contextmanager
from .schema import (CreateAccountSchema,
                     CreateAccountHolderSchema,
                     CreateResourceSchema, DeleteResourceStatusSchema, UpdateFormFactorStatusSchema,
                     UpdateResourceStatusSchema, AccountCreditSchema,
                     AccountDebitSchema, AccountTransferSchema)
from .service import OAuthService


class OAuthMicroClient(object):

    def __init__(self, oauth_service: OAuthService):
        self.oauth_service = oauth_service

    @contextmanager
    def open(self):
        try:
            self.oauth_service.open()
            yield self
        finally:
            self.oauth_service.close()

    def start(self):
        self.oauth_service.open()

    def finish(self):
        self.oauth_service.close()

    # Makes a call to oauth micro service and issues account holder
    def introspection(self, auth_token: str) -> Dict:
        response = self.oauth_service.introspection(auth_token=auth_token)
        return response

    def create_user(
        self,
        token: str,
        token_type: int,
        username: str,
        auth_key: Optional[str],
        device_id: Optional[str]
    ) -> Dict:
        response = self.oauth_service.create_user(
            token=token,
            token_type=token_type,
            auth_key=auth_key,
            username=username,
            device_id=device_id,
        )
        return response

    def get_user(
        self,
        auth_token: str
    ) -> Dict:
        response = self.oauth_service.get_user(
            auth_token=auth_token
        )
        return response

    def generate_token(
        self,
        token: str,
        token_type: int,
        auth_key: str,
    ) -> Dict:
        response = self.oauth_service.generate_token(
            token=token,
            token_type=token_type,
            auth_key=auth_key
        )
        return response

    def update_user(
        self,
        token: str,
        token_type: int,
        username: str,
        auth_key: Optional[str],
        device_id: Optional[str],
        person_id: Optional[str],
    ) -> Dict:
        response = self.oauth_service.update_user(
            token=token,
            token_type=token_type,
            auth_key=auth_key,
            username=username,
            device_id=device_id,
            person_id=person_id
        )
        return response

    def find_user_by_token(
        self,
        token: str,
        token_type: int
    ):
        response = self.oauth_service.find_user_by_token(
            token=token,
            token_type=token_type,
        )
        return response

    def find_user_by_person_id(
        self,
        person_id: str,
    ):
        response = self.oauth_service.find_user_by_person_id(
            person_id=person_id
        )
        return response

    def check_user(
        self,
        token: str,
        token_type: int,
        device_id: str,
    ):
        response = self.oauth_service.check_user(
            token=token,
            token_type=token_type,
            device_id=device_id,
        )
        return response

    def generate_otp(
        self,
        mobile_num: str,
        action: str
    ):
        response = self.oauth_service.generate_otp(
            mobile_num=mobile_num,
            action=action
        )
        return response
