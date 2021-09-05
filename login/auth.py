from login.models import User
from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication


class UserAuth(BaseAuthentication):

    def authenticate(self, request):
        if request.method == 'GET':
            token = request.query_params.get('token')
            try:
                u_id = cache.get(token)
                user = User.objects.get(pk=u_id)
                return user, token
            except:
                return
