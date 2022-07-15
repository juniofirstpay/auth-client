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
    def introspection(
            self,
            client_id: str,
            client_secret: str,
            auth_token: str,
            auth_token_type: str) -> Dict:
        response = self.oauth_service.introspection(
            client_id=client_id,
            client_secret=client_secret,
            token=auth_token,
            token_type_hint=auth_token_type
        )
        return response

    def generate_otp(
        self,
        client_id: str,
        client_secret: str,
        mobile_number: str,
        scope:str = None
    ):
        response = self.oauth_service.otp(
            client_id=client_id,
            client_secret=client_secret,
            mobile_number=mobile_number,
            action="generate",
            send_sms=True,
            scope=scope
        )
        return response

    def verify_otp(
        self,
        client_id: str,
        client_secret: str,
        mobile_number: str,
        otp_token: str,
        otp: str,
        scope: str = None
    ):
        response = self.oauth_service.otp(
            client_id=client_id,
            client_secret=client_secret,
            mobile_number=mobile_number,
            action="validate",
            otp_token=otp_token,
            otp=otp,
            send_sms=False,
            scope = scope
        )
        return response

    def validate_scope(
        self, 
        client_id: str,
        client_secret: str,
        mobile_number: str,
        scope:str,
        access_token:str
    ):

        response = self.oauth_service.validate_access(
            client_id=client_id,
            client_secret=client_secret,
            mobile_number=mobile_number,
            scope = scope,
            access_token=access_token
        )

        return response

    def authorize(
        self,
        client_id: str,
        client_secret: str,
        grant_type: str,
        scope: str,
        token: str,
        token_type: int,
        auth_key: str,
        device_id: str=None
    ):
        return self.oauth_service.authorize(
            client_id=client_id,
            client_secret=client_secret,
            grant_type=grant_type,
            scope=scope,
            username=token,
            password=auth_key,
            device_id=device_id
        )
    
    def authorize_via_otp(
        self,
        client_id: str,
        client_secret: str,
        grant_type: str,
        scope: str,
        username: str,
        otp: int,
        otp_token: str,
    ):
        return self.oauth_service.authorize_via_otp(
            client_id=client_id,
            client_secret=client_secret,
            grant_type=grant_type,
            scope=scope,
            username=username,
            otp=otp,
            otp_token=otp_token
        )

    def register(
        self,
        client_id: str,
        client_secret: str,
        device_id: str,
        token: str,
        token_type: int,
        auth_key: str,
        otp: str,
        otp_token: str,
        forgot_mpin=False,
        migration_status=1
    ):
        return self.oauth_service.register(
            client_id=client_id,
            client_secret=client_secret,
            token=token,
            token_type=token_type,
            auth_key=auth_key,
            device_id=device_id,
            otp=otp,
            otp_token=otp_token,
            forgot_mpin=forgot_mpin,
            migration_status=migration_status
        )

    def reset_auth_key(
        self,
        client_id: str,
        client_secret: str,
        device_id: str,
        token: str,
        token_type: int,
        auth_key: str,
        otp: str,
        otp_token: str
    ):
        return self.oauth_service.register(
            client_id=client_id,
            client_secret=client_secret,
            token=token,
            token_type=token_type,
            auth_key=auth_key,
            device_id=device_id,
            otp=otp,
            otp_token=otp_token,
            forgot_mpin=True
        )

    def create_user(
        self,
        token: str,
        token_type: int,
        username: Optional[str],
        auth_key: Optional[str],
        device_id: Optional[str],
        migration_status: Optional[int]
    ) -> Dict:
        response = self.oauth_service.create_user(
            token=token,
            token_type=token_type,
            auth_key=auth_key,
            username=username,
            device_id=device_id,
            migration_status=migration_status
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
        device_id: str,
    ):
        response = self.oauth_service.check_user(
            token=token,
            device_id=device_id,
        )
        return response
