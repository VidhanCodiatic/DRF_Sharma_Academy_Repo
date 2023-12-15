

from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, status, viewsets
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.throttling import (AnonRateThrottle, ScopedRateThrottle,
                                       UserRateThrottle)
from rest_framework.views import APIView

from assessment.throttle import AssessmentThrottle
from courses.models import Course, Document, EmbedLecture, Lecture, Pdf
from courses.permissions import CustomCoursePermission
from courses.serializers import (CourseSerializer, DocumentSerializer,
                                 EmbedLectureSerializer, LectureSerializer,
                                 PdfSerializer)
# from drf_yasg.utils import swagger_auto_schema

from drf_spectacular.utils import extend_schema


class CourseViewSet(viewsets.ModelViewSet):
    """
    List all Courses, create a new course with put, patch and delete.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAdminUser]

    # it will show search field in browser api
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['instructor__email']  # we can search by value
    ordering_fields = ['instructor__email']

    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
    #     context['instructor'] = self.request.user
    #     # context.update({"request": self.request})
    #     # context['additional'] = 'vidhan'
    #     # context.update({
    #     #     "name": ['test@test.com']
    #     #     # extra data
    #     # })
    #     return context

    # def create(self, request, *args, **kwargs):
    #     name = self.get_serializer_context().get('name')

    #     return super().create(request, *args, **kwargs)


class LectureModelViewSet(viewsets.ModelViewSet):
    """
    List all Lecture, create a new lecture with put, patch and delete.
    """
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = [CustomCoursePermission]

    # it will show search field in browser api
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['course__name', 'id']  # we can search by value
    ordering_fields = ['course__name', 'id']


# class PdfModelViewSet(viewsets.ModelViewSet):
#     """
#     List all Pdf's
#     """
#     queryset = Pdf.objects.all()
#     serializer_class = PdfSerializer
#     permission_classes = [CustomCoursePermission]

class PdfListAPIView(generics.ListAPIView):
    """
    List of all Pdf's.
    """
    queryset = Pdf.objects.all()
    serializer_class = PdfSerializer
    permission_classes = [CustomCoursePermission]

    # it will show search field in browser api
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['course__name']  # we can search by value
    ordering_fields = ['course__name']

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['course']
    # filterset_fields = ['instructor', 'course']

    # def get_queryset(self):
    #     """
    #     This view should return a list of all the pdf
    #     for the currently authenticated user.
    #     """
    #     user = self.request.user
    #     return Pdf.objects.filter(instructor=user)


class PdfDetailAPIView(generics.RetrieveAPIView):
    """
    Detail of specified pdf.
    """
    queryset = Pdf.objects.all()
    serializer_class = PdfSerializer
    permission_classes = [CustomCoursePermission]


class PdfCreateAPIView(generics.CreateAPIView):
    """
    Create Pdf.
    """
    queryset = Pdf.objects.all()
    serializer_class = PdfSerializer
    permission_classes = [CustomCoursePermission]


class PdfUpdateAPIView(generics.UpdateAPIView):
    """
    Update specified pdf. 
    """
    queryset = Pdf.objects.all()
    serializer_class = PdfSerializer
    permission_classes = [CustomCoursePermission]


class PdfRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    Partially update pdf.
    """
    queryset = Pdf.objects.all()
    serializer_class = PdfSerializer
    permission_classes = [CustomCoursePermission]


class PdfDestroyAPIView(generics.DestroyAPIView):
    """
    Delete pdf.
    """
    queryset = Pdf.objects.all()
    serializer_class = PdfSerializer
    permission_classes = [CustomCoursePermission]


class EmbedModelViewSet(viewsets.ModelViewSet):
    """
    List all EmbedLecture, create a new lecture with put, patch and delete.
    """
    queryset = EmbedLecture.objects.all()
    serializer_class = EmbedLectureSerializer
    permission_classes = [CustomCoursePermission]

    # it will show search field in browser api
    filter_backends = [SearchFilter]
    search_fields = ['course__name']  # we can search by value


class DocumentList(APIView):
    """
    List all document, or create a new document.
    """
    permission_classes = [CustomCoursePermission]
    # throttle_classes = [AssessmentThrottle, AnonRateThrottle]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewdoc'
    serializer_class = DocumentSerializer

    def get(self, request, format=None):
        document = Document.objects.all()
        serializer = self.serializer_class(document, many=True)
        return Response(serializer.data)

    # @swagger_auto_schema(
    #     request_body=DocumentSerializer,
    #     responses={status.HTTP_201_CREATED: DocumentSerializer},
    # )
    @extend_schema(
        request=DocumentSerializer,
        responses={201: DocumentSerializer},
    )
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentDetail(APIView):
    """
    Retrieve, update or delete a document instance.
    """
    permission_classes = [CustomCoursePermission]

    def get_object(self, pk):
        try:
            return Document.objects.get(pk=pk)
        except Document.DoesNotExist:
            raise Http404
        
    @extend_schema(
        request=DocumentSerializer,
        responses={201: DocumentSerializer},
    )
    def get(self, request, pk, format=None):
        document = self.get_object(pk)
        serializer = DocumentSerializer(document)
        return Response(serializer.data)
    
    # @swagger_auto_schema(
    #     request_body=DocumentSerializer,
    #     responses={status.HTTP_200_OK: DocumentSerializer},
    # )
    @extend_schema(
        request=DocumentSerializer,
        responses={201: DocumentSerializer},
    )
    def put(self, request, pk, format=None):
        document = self.get_object(pk)
        serializer = DocumentSerializer(document, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        document = self.get_object(pk)
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)