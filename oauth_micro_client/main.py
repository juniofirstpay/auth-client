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
    def introspection(self, token: str) -> Dict:
        response = self.oauth_service.introspection(token=token)
        return response
