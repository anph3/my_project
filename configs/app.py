import enum

class AppConfigs(enum.Enum):
    CHECK_CONNECTION_DB = 'SELECT 1'
    
class Token(enum.Enum):
    private_key = 'anphMNcZkh'
    public_key = 'fnEcdMHkm'
    jwt_secret_key = 'UOJNHKzxcxz672bnvghjquvmxjvkjlk'
    type = 'Bearer '
    hash = 'HS512'
    session_prefix = 'session:'
    tls_access_token = 3600
    tls_refresh_token = 10800