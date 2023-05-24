from rest_framework import serializers

class DatabaseInfo(serializers.Serializer):
    ENGINE = serializers.CharField(required=False)
    NAME = serializers.CharField(required=False)
    USER = serializers.CharField(required=False)
    HOST = serializers.CharField(required=False)
    PORT = serializers.CharField(required=False)
    
class RedisInfo(serializers.Serializer):
    host = serializers.CharField()
    port = serializers.CharField()
    db = serializers.CharField()
    