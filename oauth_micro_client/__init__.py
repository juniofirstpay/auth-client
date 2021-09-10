from .main import OAuthMicroClient
from .service import OAuthService
from .env import __config


def OAuthClient():
    oauth_service = OAuthService(
        __config.get('endpoint'),
        __config.get('clientid'),
        __config.get('clientsecret'),
    )
    oauth_client = OAuthMicroClient(oauth_service)
    return oauth_client