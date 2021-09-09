### OAuth Micro Service

This is a self importable package to connect to OAuth micro service, and this is implemented for code reusability purposes


#### Requirements
For client to it requires a `config.yaml` file, if one exists add the following elements
```
    variant: Dev|Prod
    service:
        endpoint: <OAuthMicroServiceEndpoint>
        clientid: <AppClientId>
        clientsecret: <AppClientSecret>
        apikey: <ApiKey>

```