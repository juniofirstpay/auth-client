import json
from yaml import FullLoader as loader, load
from warnings import warn

__variant = None
__config = None
# try:
#     env = load(open('config.yaml'), Loader=loader)
#     __config = env.get('oauth', {}).get('service')
#     __variant = env.get('oauth', {}).get('variant')

#     if __config is None:
#         warn("Config Object Not Found")

#     if __config.get('endpoint') is None:
#         warn("oAuth Client Enpoint Not Configured")

#     if __config.get('client_id') is None:
#         warn("oAuth Client Id Configured")

#     if __config.get('client_secret') is None:
#         warn("oAuth Client Secret Configured")

#     if __variant is None:
#         warn("Without variant no call will be made")


# except Exception as e:
#     print(e)
    
def setup(env):
    global __config
    global __variant
    try:
        # env = load(open('config.yaml'), Loader=loader)
        __config = env.get('oauth', {}).get('service')
        __variant = env.get('oauth', {}).get('variant')

        if __config is None:
            warn("Config Object Not Found")

        if __config.get('endpoint') is None:
            warn("oAuth Client Enpoint Not Configured")

        if __config.get('client_id') is None:
            warn("oAuth Client Id Configured")

        if __config.get('client_secret') is None:
            warn("oAuth Client Secret Configured")

        if __variant is None:
            warn("Without variant no call will be made")

    except Exception as e:
        print(e)


def get_config():
    return __config