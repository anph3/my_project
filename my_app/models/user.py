from django.db import models
from ..reponsitory.user_manage import UserManager


class User(models.Model):
    class Meta:
        db_table = 'user'
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()
    
    objects = UserManager()