from rest_framework import serializers

from assessment.models import Assessment, Choice, Question
from courses.models import Course


class AssessmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Assessment
        fields = ['id', 'url', 'course', 'title', 'duration', 'type']


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['id', 'assessment', 'question']

class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ['id', 'question', 'option', 'correct']





    # id = serializers.IntegerField(read_only=True) # also id show in data
    # course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    # title = serializers.CharField(max_length=100)
    # duration = serializers.DurationField()
    # type = serializers.CharField()

    # def create(self, validate_data):
    #     """
    #     Create and return a new `Assessment` instance, given the validated data.
    #     """
    #     return Assessment.objects.create(**validate_data)
    
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Assessment` instance, given the validated data.
    #     """
    #     instance.course = validated_data.get('course', instance.course)
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.duration = validated_data.get('duration', instance.duration)
    #     instance.type = validated_data.get('type', instance.type)
    #     instance.save()
    #     return instance
    
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