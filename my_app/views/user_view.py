from .views import *

class UserView(ViewSet):
    def all_user(self, request):
        queryset = user_m.User.objects.all_list(request=request)
        serializer = user_serializer_s.UserSerializer(queryset, many=True)
        return response_h.response_data(serializer.data)