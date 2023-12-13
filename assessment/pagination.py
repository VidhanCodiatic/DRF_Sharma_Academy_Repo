from rest_framework.pagination import (CursorPagination, LimitOffsetPagination,
                                       PageNumberPagination)


class AssessmentPagination(PageNumberPagination):
    page_size = 1
    # page_query_param = 'mypage' # for define page in url 
    # page_size_query_param = 'records' # for client set page
    # max_page_size = 7 # for user define page size limit
    # last_page_strings = 'end' # for lasr page show

class AssessmentLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit = 6

class AssessmentCurserPagination(CursorPagination):
    page_size = 2
    ordering = 'title'
    cursor_query_param = 'mycurser'
