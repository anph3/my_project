from django.db import models
from ..paginations import paginations

class UserManager(models.Manager):
    def check_is_exists(self, value):
        return self.filter(**value) 
    
    def all_list(self, request):
        queryset = self.all()
        paginator = paginations.StandardPagination()
        return paginator.paginate_queryset(queryset=queryset, request=request)