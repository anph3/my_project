from .views import *

class HealthView(ViewSet):
    def health(self, request):
        try:
            cursor = connection.cursor()
            cursor.execute(AppConfigs.CHECK_CONNECTION_DB.value)
            result = cursor.fetchone()
            if result[0] == 1:
                database = True
        except:
            return response_h.response_data(
                status=response_c.STATUS.DATABASE_CONNECT_FAILD.value, 
                message=response_c.ERROR.DB_CHECK.value
            )
        
        try:
            redis_conn = get_redis_connection(st.SESSION_CACHE_ALIAS)
            redis_conn.ping()
            redis = True
        except:
            return response_h.response_data(
                status=response_c.STATUS.DATABASE_CONNECT_FAILD.value, 
                message=response_c.ERROR.REDIS_CHECK.value
            )
        database_info = st.DATABASES['default'].copy()
        cache_backend = caches['default']
        cache_client = cache_backend.client.get_client(write=True)
        cache_info = cache_client.connection_pool.connection_kwargs
        
        validate_database = health_serializer_s.DatabaseInfo(data=database_info)
        validate_database.is_valid()
        
        validate_redis = health_serializer_s.RedisInfo(data=cache_info)
        validate_redis.is_valid()
        
        return response_h.response_data({
            'database': validate_database.data,
            'cache': validate_redis.data
        })