

from rest_framework import generics, status, viewsets, filters
from rest_framework.response import Response

from assessment.models import Assessment, Choice, Question
from assessment.pagination import (AssessmentLimitOffsetPagination,
                                   AssessmentPagination)
from assessment.permissions import CustomAssessmentPermission
from assessment.serializers import (AssessmentSerializer, ChoiceSerializer,
                                    QuestionSerializer)
# from drf_yasg.utils import swagger_auto_schema

from drf_spectacular.utils import extend_schema


class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = [CustomAssessmentPermission]

    filter_backends = [filters.SearchFilter] # it will show search field in browser api
    search_fields = ['title'] # we can search by value


class QuestionViewSet(viewsets.ViewSet):

    permission_classes = [CustomAssessmentPermission]

    # filter_backends = [filters.SearchFilter] # it will show search field in browser api
    # search_fields = ['assessment'] # we can search by value

    def list(self, request):
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            if pk is not None:
                question = Question.objects.get(pk=pk)
                serializer = QuestionSerializer(question)
                return Response(serializer.data)
        except Exception as e:
            return Response({'error' : str(e)})
        
    # @swagger_auto_schema(
    #   request_body=QuestionSerializer,
    #   responses={status.HTTP_201_CREATED: QuestionSerializer}
    # )

    @extend_schema(
        request=QuestionSerializer,
        responses={201: QuestionSerializer},
    )
    def create(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # @swagger_auto_schema(
    #   request_body=QuestionSerializer,
    #   responses={status.HTTP_200_OK: QuestionSerializer}
    # )
    @extend_schema(
        request=QuestionSerializer,
        responses={200: QuestionSerializer},
    )
    def update(self, request, pk=None):
        question = Question.objects.get(pk=pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # @swagger_auto_schema(
    #   request_body=QuestionSerializer,
    #   responses={status.HTTP_201_CREATED: QuestionSerializer}
    # )
    @extend_schema(
        request=QuestionSerializer,
        responses={200: QuestionSerializer},
    )
    def partial_update(self, request, pk=None):
        question = Question.objects.get(pk=pk)
        serializer = QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Partial Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({'msg' : 'Data Deleted'})


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [CustomAssessmentPermission]
    # pagination_class = AssessmentPagination
    pagination_class = AssessmentLimitOffsetPagination
    


class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [CustomAssessmentPermission]
