DEBUG = True

# date format

DATE_FORMAT = '%d-%m-%Y'

TIME_FORMAT = '%H:%M:%S'

DATETIME_FORMAT = '%d-%m-%Y {}'.format(TIME_FORMAT)

DATE_INPUT_FORMATS = [
    '%d/%m/%Y',
    '%Y-%m-%d',
    '%d-%m-%Y',
    '%Y/%m/%d'
]

DATETIME_INPUT_FORMATS = [
    '%Y-%m-%d {}'.format(TIME_FORMAT),
    '%Y/%m/%d {}'.format(TIME_FORMAT),
    '%d-%m-%Y {}'.format(TIME_FORMAT),
    '%d/%m/%Y {}'.format(TIME_FORMAT)
] + DATE_INPUT_FORMATS

REST_FRAMEWORK = {
    'DATE_FORMAT': DATE_FORMAT,
    'DATETIME_FORMAT': DATETIME_FORMAT,
    'DATE_INPUT_FORMATS': DATE_INPUT_FORMATS,
    'DATETIME_INPUT_FORMATS': DATETIME_INPUT_FORMATS,
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FormParser'
    ]
}

# middleware

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'middleware.login_middleware.AuthUserMiddleware',
]

NAME = 'auth' 
USER = 'root' 
PASSWORD = ''
HOST = 'localhost'
PORT = '3306'

REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6379'
REDIS_DB = '15'