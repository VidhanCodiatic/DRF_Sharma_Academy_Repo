from rest_framework.throttling import UserRateThrottle

class CourseThrottle(UserRateThrottle):
    scope = 'course'