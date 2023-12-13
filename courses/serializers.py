

from rest_framework import serializers
from users.models import CustomUser
from rest_framework.response import Response

from courses.models import Course, Document, EmbedLecture, Lecture, Pdf


class InstructorSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['email']

class CourseSerializer(serializers.ModelSerializer):
    instructorMail = serializers.CharField(source = 'instructor.email', read_only=True)
    # instructor = serializers.HyperlinkedIdentityField(view_name='user-detail')
    # instructor = serializers.SlugRelatedField(read_only=True, slug_field='email')
    # instructor = InstructorSerializer(many=True, read_only=True)
    # instructor = serializers.SerializerMethodField()
    # instructor = serializers.StringRelatedField(read_only=True)
    # instructor = serializers.ReadOnlyField()

    class Meta:
        model = Course
        fields = ['id', 'instructorMail','instructor', 'name', 'image', 'duration', 
                  'fees', 'type', 'description',
        ]
        extra_kwargs = {'instructor': {'write_only': True}}
    
    # def get_instructor(self, obj): 
    #     return obj.instructor.email if obj.instructor else None

    # def create(self, validated_data):
    #     # user = self.context["request"].user
    #     name = self.context["name"]
    #     print(f"User is: {name}")
        

class LectureSerializer(serializers.ModelSerializer):

    courseName = serializers.CharField(source = 'course.name', read_only=True)
    class Meta:
        model = Lecture
        fields = ['id', 'courseName', 'instructor', 'course', 'title', 'duration', 'lecture']
        extra_kwargs = {'course': {'write_only': True}}

class PdfSerializer(serializers.ModelSerializer):

    courseName = serializers.CharField(source = 'course.name', read_only=True)
    class Meta:
        model = Pdf
        fields = ['id', 'courseName', 'instructor', 'course', 'title', 'page', 'file']
        extra_kwargs = {'course': {'write_only': True}}

class EmbedLectureSerializer(serializers.ModelSerializer):

    courseName = serializers.CharField(source = 'course.name', read_only=True)
    class Meta:
        model = EmbedLecture
        fields = ['id', 'courseName', 'instructor', 'course', 'title', 'duration', 'url']
        extra_kwargs = {'course': {'write_only': True}}


class DocumentSerializer(serializers.ModelSerializer):

    courseName = serializers.CharField(source = 'course.name', read_only=True)
    class Meta:
        model = Document
        fields = ['id', 'courseName', 'instructor', 'course', 'title', 'url']
        extra_kwargs = {'course': {'write_only': True}}
