from rest_framework.throttling import UserRateThrottle

class AssessmentThrottle(UserRateThrottle):
    scope = 'assessment'