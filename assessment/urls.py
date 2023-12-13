

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from assessment.views import (AssessmentViewSet, ChoiceDetail, ChoiceList,
                              QuestionViewSet)

router = DefaultRouter()

router.register('assessment', AssessmentViewSet, basename='assessment')
router.register('question', QuestionViewSet, basename='question')
# router.register('choice', ChoiceModelViewSet, basename='choice')

urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')), # for user's login and logout
    
    path('api/', include(router.urls)), #for router urls
    path('api/choice/', ChoiceList.as_view(), name='choices'),
    path('api/choice/<int:pk>/', ChoiceDetail.as_view(), name='choice'),
]