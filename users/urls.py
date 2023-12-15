from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import CustomUserViewSet

userRouter = DefaultRouter()
userRouter.register(r'user', CustomUserViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')), # for user's login and logout
    path('', include(userRouter.urls)), #for userRouter urls
]