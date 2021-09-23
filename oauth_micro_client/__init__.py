from .main import OAuthMicroClient
from .service import OAuthService
from .env import __config


def OAuthClient():
    oauth_service = OAuthService(
        __config.get('endpoint'),
        __config.get('client_id'),
        __config.get('client_secret'),
        __config.get('api_key')
    )
    oauth_client = OAuthMicroClient(oauth_service)
    return oauth_client
