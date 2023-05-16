from .views import *

class HealthView(ViewSet):
    def health(self, request):
        database = redis = False
        
        try:
            cursor = connection.cursor()
            cursor.execute(AppConfigs.CHECK_CONNECTION_DB.value)
            result = cursor.fetchone()
            if result[0] == 1:
                database = True
        except:
            print(response_c.ERROR.DB_CHECK.value)
        
        try:
            redis_conn = get_redis_connection(st.SESSION_CACHE_ALIAS)
            redis_conn.ping()
            redis = True
        except:
            print(response_c.ERROR.REDIS_CHECK.value)
            
        if database and redis:
            database_info = st.DATABASES['default'].copy()
            cache_backend = caches['default']
            cache_client = cache_backend.client.get_client(write=True)
            cache_info = cache_client.connection_pool.connection_kwargs
            
            print(database_info)
            
            validate_database = health_va.DatabaseInfo(data=database_info)
            validate_database.is_valid()
            
            validate_redis = health_va.RedisInfo(data=cache_info)
            validate_redis.is_valid()
            
            return response_h.response_data({
                'database': validate_database.data,
                'cache': validate_redis.data
            })
        return response_h.response_data()