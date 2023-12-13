

from users.models import CustomUser
from users.serializers import CustomUserSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from users.permissions import CustomUserPermission



class CustomUserViewSet(viewsets.ModelViewSet):
    """
    Create or get custom user data using CustomUserPermission
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [CustomUserPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']

    #     """
    # List all EmbedLecture, create a new lecture with put, patch and delete.
    # """












    # for apiview
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView

# from users.permissions import CustomUserPermission
# from users.authentication import CustomUserAuthentication

# from rest_framework.authentication import (BasicAuthentication,
#                                            SessionAuthentication, TokenAuthentication)

    # for SessionAuthentication with CustomUserPermission
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [CustomUserPermission]

    # # for BasicAuthentication with CustomUserPermission
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [CustomUserPermission]

    # # for TokenAuthentication with CustomUserPermission
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [CustomUserPermission]

    # for JWTAuthentication with CustomUserPermission
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [CustomUserPermission]
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.AllowAny]

    # authentication_classes = [CustomUserAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    # def list(self, request):
    #     customuser = CustomUser.objects.all()
    #     print(customuser)
    #     serializer = CustomUserSerializer(customuser, many=True)
    #     print(serializer.data)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     try:
    #         id = pk
    #         if id is not None:
    #             customuser = CustomUser.objects.get(pk=id)
    #             serializer = CustomUserSerializer(customuser)
    #             return Response(serializer.data)
    #     except Exception as e:
    #         return Response({'error' : str(e)})
     
    # def create(self, request):
    #     serializer = CustomUserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg' : 'Data Created'}, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def update(self, request, pk=None):
    #     id = pk
    #     customuser = CustomUser.objects.get(pk=id)
    #     serializer = CustomUserSerializer(customuser, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg' : 'Data Updated'})
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def partial_update(self, request, pk=None):
    #     id = pk
    #     customuser = CustomUser.objects.get(pk=id)
    #     serializer = CustomUserSerializer(customuser, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg' : 'Partial Data Updated'})
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def destroy(self, request, pk=None):
    #     id = pk
    #     customuser = CustomUser.objects.get(pk=id)
    #     customuser.delete()
    #     return Response({'msg' : 'Data Deleted'})


# def assessment_detail(request, pk):
#     assessment = Assessment.objects.get(id=pk)
#     serializer = AssessmentSerializer(assessment)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type='application/json')

# def assessment_list(request):
#     assessment = Assessment.objects.all()
#     serializer = AssessmentSerializer(assessment, many=True)
#     # json_data = JSONRenderer().render(serializer.data)
#     # return HttpResponse(json_data, content_type='application/json')
#     return JsonResponse(serializer.data, safe=False)

# @csrf_exempt
# def assessment_create(request):
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer = AssessmentSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg' : 'Data created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')

#     return HttpResponse('method not post')


# @csrf_exempt
# def assessment_update(request, pk):

#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         assessment = Assessment.objects.get(id=pk)
#         serializer = AssessmentSerializer(assessment, data=python_data, partial=True)
#         # serializer = AssessmentSerializer(assessment, data=python_data) # for fully updated
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg' : 'Data updated'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')

#     return HttpResponse('method not put')

# @csrf_exempt
# def assessment_delete(request, pk):

#     if request.method == 'DELETE':
#         assessment = Assessment.objects.get(id=pk)
#         assessment.delete()
#         res = {'msg' : 'Data deleted'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type='application/json')

# @api_view(['GET', 'POST'])
# def question_list(request):
#     """
#     List all questions, or create a new question.
#     """
#     if request.method == 'GET':
#         questions = Question.objects.all()
#         serializer = QuestionSerializer(questions, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = QuestionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def question_detail(request, pk):
#     """
#     Retrieve, update or delete a question.
#     """
#     try:
#         question = Question.objects.get(pk=pk)
#     except Question.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = QuestionSerializer(question)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = QuestionSerializer(question, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # @api_view(['GET', 'PUT', 'DELETE'])
# # def choice_detail(request, pk):
# #     """
# #     Retrieve, update or delete a code snippet.
# #     """
# #     try:
# #         choice = Choice.objects.get(pk=pk)
# #     except Choice.DoesNotExist:
# #         return Response(status=status.HTTP_404_NOT_FOUND)

# #     if request.method == 'GET':
# #         serializer = ChoiceSerializer(choice)
# #         return Response(serializer.data)

# #     elif request.method == 'PUT':
# #         serializer = ChoiceSerializer(choice, data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     elif request.method == 'DELETE':
# #         choice.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)



# from rest_framework import mixins
# from rest_framework import generics

# class ChList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Choice.objects.all()
#     serializer_class = ChoiceSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ChDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Choice.objects.all()
#     serializer_class = ChoiceSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)




# import json
# import io
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from assessment.serializers import AssessmentSerializer, QuestionSerializer, ChoiceSerializer
# from django.views.decorators.csrf import csrf_exempt

# # for apiview
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView


# def assessment_detail(request, pk):
#     assessment = Assessment.objects.get(id=pk)
#     serializer = AssessmentSerializer(assessment)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type='application/json')

# def assessment_list(request):
#     assessment = Assessment.objects.all()
#     serializer = AssessmentSerializer(assessment, many=True)
#     # json_data = JSONRenderer().render(serializer.data)
#     # return HttpResponse(json_data, content_type='application/json')
#     return JsonResponse(serializer.data, safe=False)

# @csrf_exempt
# def assessment_create(request):
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer = AssessmentSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg' : 'Data created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json') 
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
    
#     return HttpResponse('method not post')
    

# @csrf_exempt
# def assessment_update(request, pk):
    
#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         assessment = Assessment.objects.get(id=pk)
#         serializer = AssessmentSerializer(assessment, data=python_data, partial=True)
#         # serializer = AssessmentSerializer(assessment, data=python_data) # for fully updated
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg' : 'Data updated'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')

#     return HttpResponse('method not put')

# @csrf_exempt
# def assessment_delete(request, pk):

#     if request.method == 'DELETE':
#         assessment = Assessment.objects.get(id=pk)
#         assessment.delete()
#         res = {'msg' : 'Data deleted'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type='application/json')
    
# @api_view(['GET', 'POST'])
# def question_list(request):
#     """
#     List all questions, or create a new question.
#     """
#     if request.method == 'GET':
#         questions = Question.objects.all()
#         serializer = QuestionSerializer(questions, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = QuestionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def question_detail(request, pk):
#     """
#     Retrieve, update or delete a question.
#     """
#     try:
#         question = Question.objects.get(pk=pk)
#     except Question.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = QuestionSerializer(question)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = QuestionSerializer(question, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# @api_view(['GET', 'PUT', 'DELETE'])
# def choice_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         choice = Choice.objects.get(pk=pk)
#     except Choice.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ChoiceSerializer(choice)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ChoiceSerializer(choice, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         choice.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    



# class ChoiceList(APIView):
#     """
#     List all assessment, or create a new choice.
#     """
#     def get(self, request, format=None):
#         choice = Choice.objects.all()
#         serializer = ChoiceSerializer(choice, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ChoiceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# from django.http import Http404

# class ChoiceDetail(APIView):
#     """
#     Retrieve, update or delete a choice instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Choice.objects.get(pk=pk)
#         except Choice.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         choice = self.get_object(pk)
#         serializer = ChoiceSerializer(choice)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         choice = self.get_object(pk)
#         serializer = ChoiceSerializer(choice, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         choice = self.get_object(pk)
#         choice.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# from rest_framework import mixins
# from rest_framework import generics

# class ChList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Choice.objects.all()
#     serializer_class = ChoiceSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class ChDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Choice.objects.all()
#     serializer_class = ChoiceSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    



# class QList(generics.ListCreateAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer


# class QDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer


# from rest_framework import viewsets

# class QuestionViewSet(viewsets.ViewSet):

#     def list(self, request):
#         question = Question.objects.all()
#         serializer = QuestionSerializer(question, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         try:
#             id = pk
#             if id is not None:
#                 question = Question.objects.get(pk=id)
#                 serializer = QuestionSerializer(question)
#                 return Response(serializer.data)
#         except Exception as e:
#             return Response({'error' : str(e)})
        
#     def create(self, request):
#         serializer = QuestionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg' : 'Data Created'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

#     def update(self, request, pk=None):
#         id = pk
#         question = Question.objects.get(pk=id)
#         serializer = QuestionSerializer(question, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg' : 'Data Updated'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def partial_update(self, request, pk=None):
#         id = pk
#         question = Question.objects.get(pk=id)
#         serializer = QuestionSerializer(question, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg' : 'Partial Data Updated'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         id = pk
#         question = Question.objects.get(pk=id)
#         question.delete()
#         return Response({'msg' : 'Data Deleted'})
    
# from rest_framework.authentication import BasicAuthentication, SessionAuthentication
# from rest_framework import permissions

# class QuestionModelViewSet(viewsets.ModelViewSet):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
    # authentication_classes = [BasicAuthentication]
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAdminUser]
    # permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes = [permissions.DjangoModelPermissions]
    # permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]



# settings.py file
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.BasicAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#     ]
# }
