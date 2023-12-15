

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from assessment.views import (AssessmentViewSet, ChoiceDetail, ChoiceList,
                              QuestionViewSet)

router = DefaultRouter()

router.register(r'assessment', AssessmentViewSet, basename='assessment')
router.register(r'question', QuestionViewSet, basename='question')
# router.register('choice', ChoiceModelViewSet, basename='choice')

urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')), # for user's login and logout
    
    path('', include(router.urls)), #for router urls
    path('choice/', ChoiceList.as_view(), name='choices'),
    path('choice/<int:pk>/', ChoiceDetail.as_view(), name='choice'),
]