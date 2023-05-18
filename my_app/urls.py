from django.urls import path, include
import os

from helpers import response as rh


if os.getenv('APP_ENV', 'local') != 'local':
    from helpers.system import import_configs
    import_configs('view','v' ,'my_app')
    from helpers.system import *
else:
    from helpers.system import (content_file_import, create_file)

    imported_configs = ''
    imported_configs += content_file_import('view', 'v','my_app')
    create_file(imported_configs, '/import_view.py', os.path.dirname(os.path.abspath(__file__)))
    
    from .import_view import *

all_url = {
    'url_health':[
        path('health', health_check_view_v.HealthView.as_view({'get':'health'}), name='health'),
        path('test', health_check_view_v.HealthView.as_view({'get':'test'}), name='test'),
    ],
}

url_item = []

for item in all_url:
    url_item += all_url[item]
    
urlpatterns = [
    path('my-project/', include(url_item))
]

handler404 = rh.custom404