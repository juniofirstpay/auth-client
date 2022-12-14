from .main import OAuthMicroClient
from .service import OAuthService
from .env import get_config


def OAuthClient():
    config = get_config()
    oauth_service = OAuthService(
        config.get('endpoint'),
        config.get('client_id'),
        config.get('client_secret'),
        config.get('api_key')
    )
    oauth_client = OAuthMicroClient(oauth_service)
    return oauth_client
