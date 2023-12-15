"""
URL configuration for DRF_Sharma_Academy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

# from users.token import CustomAuthToken
# from rest_framework.authtoken import views


# from django.conf.urls.static import static
# from rest_framework_swagger.views import get_swagger_view
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from rest_framework import permissions
# from django.conf import settings

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Sharma Academy",
#         default_version='v1',
#         description = "your api",
#         ),
#     public=True,
# permission_classes=(permissions.AllowAny,),
# )

# schema_view = get_swagger_view(
#     title = "Sharma Aca"
# )


from drf_spectacular.views import (SpectacularAPIView,
                                   SpectacularRedocView, SpectacularSwaggerView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('courses.urls')),
    path('', include('assessment.urls')),

    # path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'), # for auth token
    # path('api-token-custom/', CustomAuthToken.as_view()), # for Custom auth token

    path('token/generate/', TokenObtainPairView.as_view(),
         name='token'),  # from jwt get token
    path('token/refresh/', TokenRefreshView.as_view(),
         name='refresh'),  # from jwt refresh token
    path('token/verify/', TokenVerifyView.as_view(),
         name='verify'),  # from jwt verify token

    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # path('doc/', schema_view)
    # path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
