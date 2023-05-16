# module libary
from rest_framework.viewsets import ViewSet
from django.db import connection
from django_redis import get_redis_connection
from django.conf import settings as st
from configs.app import AppConfigs
from django.core.cache import cache
from django.core.cache import caches

import os
from configs.system import (DIRECTORY_STRUCTURE, DIRECTORY_STRUCTURE_MYAPP)

# ctr + click navigate
# import inspect

# auto import
if os.getenv('APP_ENV', 'local') != 'local':
    from helpers.system import import_configs

    for key, value in DIRECTORY_STRUCTURE.items():
        import_configs(key, value)
        
    for key, value in DIRECTORY_STRUCTURE_MYAPP.items():
        import_configs(key, value, 'my_app')
        
    from helpers.system import *
else:
    from helpers.system import (content_file_import, create_file)
    
    imported_configs = ''
    
    for key, value in DIRECTORY_STRUCTURE.items():
        imported_configs += content_file_import(key, value)
        
    for key, value in DIRECTORY_STRUCTURE_MYAPP.items():
        imported_configs += content_file_import(key, value, 'my_app')
    
    create_file(imported_configs)
    
    from .auto_import import *