from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.models import CustomUser

# from assessment.models import Assessment, Question, Choice
# from courses.models import Course

class CustomUserSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True) # also id show in data
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'phone', 'email', 'password', 'type']
        # read_only_fields = ['account_name']
        # extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(CustomUserSerializer, self).create(validated_data)
    
# class CustomUserLoginSerializer(serializers.ModelSerializer):



#     course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
#     duration = serializers.DurationField()


# class AssessmentSerializer(serializers.Serializer):

#     id = serializers.IntegerField(read_only=True) # also id show in data
#     course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
#     title = serializers.CharField(max_length=100)
#     duration = serializers.DurationField()
#     type = serializers.CharField()

#     def create(self, validate_data):
#         """
#         Create and return a new `Assessment` instance, given the validated data.
#         """
#         return Assessment.objects.create(**validate_data)
    
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Assessment` instance, given the validated data.
#         """
#         instance.course = validated_data.get('course', instance.course)
#         instance.title = validated_data.get('title', instance.title)
#         instance.duration = validated_data.get('duration', instance.duration)
#         instance.type = validated_data.get('type', instance.type)
#         instance.save()
#         return instance
    
# class QuestionSerializer(serializers.Serializer):

#     id = serializers.IntegerField(read_only=True)
#     assessment = serializers.PrimaryKeyRelatedField(queryset=Assessment.objects.all())
#     question = serializers.CharField(max_length=255)

#     def create(self, validated_data):
#         """
#         Create and return a new `Question` instance, given the validated data.
#         """
#         return Question.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Question` instance, given the validated data.
#         """
#         instance.assessment = validated_data.get('assessment', instance.assessment)
#         instance.question = validated_data.get('question', instance.question)
#         instance.save()
#         return instance
    
# class ChoiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Choice
#         fields = ['id', 'question', 'option', 'correct']