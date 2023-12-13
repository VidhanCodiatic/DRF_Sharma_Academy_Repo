from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import CustomUserViewSet

userRouter = DefaultRouter()
userRouter.register('user', CustomUserViewSet, basename='user')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')), # for user's login and logout
    path('api/', include(userRouter.urls)), #for userRouter urls
]