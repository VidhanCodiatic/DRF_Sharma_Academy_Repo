
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from users.models import CustomUser


class CustomUserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        email = request.GET.get('email')
        if email is None:
            return None
        
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise AuthenticationFailed('No such user')
        return (user, None)