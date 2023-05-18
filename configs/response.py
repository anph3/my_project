import enum

class ResponseKey(enum.Enum):
    STATUS_CODE = 'statusCode'
    MESSAGE = 'message'
    DATA = 'data'
    MAX_PAGE = 'maxPage'
    LIST_DATA = 'listData'

class STATUS(enum.Enum):
    SUCCESS = 1
    ACCESS_TOKEN_FAILED = 3
    INPUT_INVALID = 4
    PAGE_NOT_FOUND = 404
    SESSION_EXPIRED = 7
    CONN_REDIS_FAILED = 8
    
class SUCCESS(enum.Enum):
    SUCCESS = 'Success'
    
class ERROR(enum.Enum):
    # health check
    DB_CHECK = 'MySQL connection failed.'
    REDIS_CHECK = 'Redis connection failed.'
    
    # middleware
    PAGE_NOT_FOUND = 'The urls was not found.'
    NOT_LOGIN = 'Not logged in, token is null.'
    AC_IS_VALID = 'AccessToken is invalid.'
    AC_NOT_DEFINE = 'AccessToken is not defined correctly.'
    SESSION_EXPIRED = 'Session expired.'

SEPARATE_THE_ERROR = '<br/>'