from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = [
            'id',
            'username',
            'password',
            'email',
            'role',
            'school'
        ]

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):

        user = CustomerUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            role=validated_data['role'],
            school=validated_data['school']
        )

        return user


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):

        user = authenticate(
            username=data['username'],
            password=data['password']
        )

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        data['user'] = user
        return data


class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = "__all__"


class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"





#####################################################################


class ExamCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ExamCategory
        fields = "__all__"


class ExamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exam
        fields = "__all__"


class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = "__all__"



class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = "__all__"


class StudentPromotionSerializer(serializers.Serializer):

    student = serializers.IntegerField()

    new_classroom = serializers.IntegerField()

    new_stream = serializers.IntegerField()





class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = "__all__"


class FeeStructureSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeeStructure
        fields = "__all__"


class FeePaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeePayment
        fields = "__all__"



class TimetableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timetable
        fields = "__all__"



class GradingSerializer(serializers.ModelSerializer):

    class Meta:
        model = GradingSystem
        fields = "__all__"
    