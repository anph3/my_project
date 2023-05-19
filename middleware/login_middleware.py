from django.middleware.security import *
from helpers.response import *
from configs import routing as rt
from configs import response as rsp
from configs import app
from my_app import urls
from django.urls import resolve
from helpers.redis import CacheRedis
import jwt

class AuthUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_url = resolve(request.path_info).url_name
        
        list_url = []
        for item in rt.GROUP_URL:
            list_url += self.get_list_url(item)
            
        if current_url in list_url:
            return self.get_response(request)
        
        header_token = request.headers.get('Authorization')
        if header_token is None:
            return json_response(status=rsp.STATUS.ACCESS_TOKEN_FAILED.value, message=rsp.ERROR.NOT_LOGIN.value)

        header_token = header_token.replace(app.Token.type.value, '')
        data_decode = jwt.decode(
            header_token, 
            app.Token.jwt_secret_key.value,
            algorithms=app.Token.hash.value, 
            options={'verify_signature': False}
        )   
        if data_decode is None:
            return json_response(status=rsp.STATUS.INPUT_INVALID.value, message=rsp.ERROR.AC_IS_VALID.value)
        
        jti = data_decode.get('jti', None)
        if jti is None:
            return json_response(status=rsp.STATUS.ACCESS_TOKEN_FAILED.value, message=rsp.ERROR.AC_NOT_DEFINE.value)
        redis_conn = CacheRedis()
        session = redis_conn.check_auth_data(jti)
        if session is None:
            return json_response(status=rsp.STATUS.SESSION_EXPIRED.value, message=rsp.ERROR.SESSION_EXPIRED.value)
        
        return self.get_response(request)
    
    def get_list_url(self, value):
        list_url = []
        for item in urls.all_url[value]:
            str_url = str(item.name)
            list_url.append(str_url)
        return list_url
