from rest_framework import serializers
from ..models.user import User
from .action_serializer import ActionSerializer

class UserSerializer(serializers.ModelSerializer, ActionSerializer):
    
    # ============================= function contructor =======================
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        pw_hidden = kwargs.pop('pw_hidden', True)
        super().__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        if pw_hidden:
            self.fields.pop("password")
    # ============================== end contructor ===========================
    
    class Meta:
        model = User
        fields = "__all__"
