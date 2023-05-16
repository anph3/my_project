import enum

class ResponseKey(enum.Enum):
    STATUS_CODE = 'statusCode'
    MESSAGE = 'message'
    DATA = 'data'
    MAX_PAGE = 'maxPage'
    LIST_DATA = 'listData'

class STATUS(enum.Enum):
    SUCCESS = 1
    INPUT_INVALID = 4
    
class SUCCESS(enum.Enum):
    SUCCESS = 'Success'
    
class ERROR(enum.Enum):
    DB_CHECK = 'MySQL connection failed'
    REDIS_CHECK = 'Redis connection failed'

SEPARATE_THE_ERROR = '<br/>'