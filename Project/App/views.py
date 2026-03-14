from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *


from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib import messages
from .models import *

#import numpy as np
#from scipy.optimize import linprog
from django.http import HttpResponse
from datetime import datetime, timedelta
#import pyotp
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random
import os
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
import requests

from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView

#---------------------FUNCTION VIEW-------------------------
from rest_framework.decorators import api_view

#------------------------CLASS BASED VIEW-------------------
from rest_framework.views import APIView



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



import jwt, datetime
from rest_framework.exceptions import AuthenticationFailed


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from App.serializers import *


#REST FRAMEWORK
from rest_framework import status
from rest_framework.response import Response

#---------------------FUNCTION VIEW-------------------------
from rest_framework.decorators import api_view

#------------------------CLASS BASED VIEW-------------------
from rest_framework.views import APIView


#------------------------GENERIC VIEWs-------------------
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


#------------------------ VIEW SETS-------------------
from rest_framework.viewsets import ModelViewSet


#------FILTERS, SEARCH AND ORDERING
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter,OrderingFilter

#------PAGINATION-------------
from rest_framework.pagination import PageNumberPagination

from django.core.mail import send_mail
from django.conf import settings

from django.core.mail import send_mail
from django.conf import settings
#----------------CREATING A CART------------------------
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from App.serializers import *

from drf_yasg.utils import swagger_auto_schema

from rest_framework import generics,status
from rest_framework.decorators import api_view
from django.db.models import Sum
from django.db import transaction
from django.utils.timezone import now, timedelta
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


import requests
from requests.auth import HTTPBasicAuth  
import requests
from django.http import JsonResponse

from dotenv import load_dotenv
import os

import requests

import base64
import requests
# AddResult
from reportlab.pdfgen import canvas
from django.http import HttpResponse

from .helpers import get_grade
#Result
# Load environment variables
load_dotenv()

class LatestVersionView(APIView):
    def get(self, request):
        latest_version = "1"
        return JsonResponse({"latest_version": latest_version})


class RegisterUser(APIView):

    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():

            user = serializer.save()

            token = Token.objects.create(user=user)

            return Response({
                "token": token.key,
                "user": serializer.data
            })

        return Response(serializer.errors)


class LoginUser(APIView):

    def post(self, request):

        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():

            user = serializer.validated_data['user']

            token, created = Token.objects.get_or_create(user=user)

            return Response({
                "token": token.key
            })

        return Response(serializer.errors)


class CreateSchool(APIView):

    def post(self, request):

        serializer = SchoolSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class CreateClassRoom(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data.copy()

        data['school'] = request.user.school.id

        serializer = ClassRoomSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class GetClasses(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        classes = ClassRoom.objects.filter(
            school=request.user.school
        )

        serializer = ClassRoomSerializer(classes, many=True)

        return Response(serializer.data)


class CreateStream(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = StreamSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class GetStreams(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, class_id):

        streams = Stream.objects.filter(
            classroom_id=class_id
        )

        serializer = StreamSerializer(streams, many=True)

        return Response(serializer.data)


class CreateStudent(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data.copy()

        data['school'] = request.user.school.id

        serializer = StudentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class GetStudents(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        students = Student.objects.filter(
            school=request.user.school
        )

        serializer = StudentSerializer(students, many=True)

        return Response(serializer.data)









####################################################################################




class CreateSubject(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data.copy()

        data['school'] = request.user.school.id

        serializer = SubjectSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class GetSubjects(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        subjects = Subject.objects.filter(
            school=request.user.school
        )

        serializer = SubjectSerializer(subjects, many=True)

        return Response(serializer.data)


class CreateExamCategory(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = ExamCategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class GetExamCategories(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        categories = ExamCategory.objects.all()

        serializer = ExamCategorySerializer(categories, many=True)

        return Response(serializer.data)


class CreateExam(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data.copy()

        data['school'] = request.user.school.id

        serializer = ExamSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class GetExams(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        exams = Exam.objects.filter(
            school=request.user.school
        )

        serializer = ExamSerializer(exams, many=True)

        return Response(serializer.data)


# class AddResult(APIView):

#     permission_classes = [IsAuthenticated]

#     def post(self, request):

#         data = request.data.copy()

#         data['school'] = request.user.school.id

#         serializer = ResultSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors)

from .helpers import get_grade

class AddResult(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data.copy()

        data['school'] = request.user.school.id

        score = data.get("marks")

        grade = get_grade(int(score), request.user.school)

        data["grade"] = grade

        serializer = ResultSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

# class BulkResultUpload(APIView):

#     permission_classes = [IsAuthenticated]

#     def post(self, request):

#         results = request.data

#         for item in results:

#             Result.objects.create(
#                 school=request.user.school,
#                 student_id=item["student"],
#                 subject_id=item["subject"],
#                 exam_id=item["exam"],
#                 marks=item["marks"]
#             )

#         return Response({"message": "Results saved successfully"})

from .helpers import get_grade

class BulkResultUpload(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        results = request.data

        for item in results:

            score = item["marks"]

            grade = get_grade(int(score), request.user.school)

            Result.objects.create(
                school=request.user.school,
                student_id=item["student"],
                subject_id=item["subject"],
                exam_id=item["exam"],
                marks=score,
                grade=grade
            )

        return Response({"message": "Results saved successfully"})

class GetStudentResults(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, student_id):

        results = Result.objects.filter(
            student_id=student_id,
            school=request.user.school
        )

        serializer = ResultSerializer(results, many=True)

        return Response(serializer.data)


class GetExamResults(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, exam_id):

        results = Result.objects.filter(
            exam_id=exam_id,
            school=request.user.school
        )

        serializer = ResultSerializer(results, many=True)

        return Response(serializer.data)





#################RANKING ####################################

class StudentReportCard(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, student_id, exam_id):

        student = Student.objects.get(id=student_id)

        results = Result.objects.filter(
            student_id=student_id,
            exam_id=exam_id,
            school=request.user.school
        )

        subjects = []
        total = 0
        count = 0

        for r in results:

            subjects.append({
                "subject": r.subject.name,
                "marks": r.marks
            })

            total += r.marks
            count += 1

        average = total / count if count > 0 else 0

        return Response({
            "student": f"{student.first_name} {student.last_name}",
            "subjects": subjects,
            "total_marks": total,
            "average": average
        })


class ClassRanking(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, class_id, exam_id):

        students = Student.objects.filter(
            classroom_id=class_id,
            school=request.user.school
        )

        data = []

        for student in students:

            results = Result.objects.filter(
                student=student,
                exam_id=exam_id
            )

            total = 0
            count = 0

            for r in results:
                total += r.marks
                count += 1

            average = total / count if count > 0 else 0

            data.append({
                "student_id": student.id,
                "name": f"{student.first_name} {student.last_name}",
                "average": average
            })

        sorted_data = sorted(
            data,
            key=lambda x: x["average"],
            reverse=True
        )

        position = 1

        for item in sorted_data:
            item["position"] = position
            position += 1

        return Response(sorted_data)



class StreamRanking(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, stream_id, exam_id):

        students = Student.objects.filter(
            stream_id=stream_id,
            school=request.user.school
        )

        data = []

        for student in students:

            results = Result.objects.filter(
                student=student,
                exam_id=exam_id
            )

            total = 0
            count = 0

            for r in results:
                total += r.marks
                count += 1

            average = total / count if count > 0 else 0

            data.append({
                "student_id": student.id,
                "name": f"{student.first_name} {student.last_name}",
                "average": average
            })

        sorted_data = sorted(
            data,
            key=lambda x: x["average"],
            reverse=True
        )

        position = 1

        for item in sorted_data:
            item["position"] = position
            position += 1

        return Response(sorted_data)



############ TO 10 Students ################

class TopStudents(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, class_id, exam_id):

        students = Student.objects.filter(
            classroom_id=class_id,
            school=request.user.school
        )

        data = []

        for student in students:

            results = Result.objects.filter(
                student=student,
                exam_id=exam_id
            )

            total = 0
            count = 0

            for r in results:
                total += r.marks
                count += 1

            average = total / count if count > 0 else 0

            data.append({
                "student": f"{student.first_name} {student.last_name}",
                "average": average
            })

        sorted_data = sorted(
            data,
            key=lambda x: x["average"],
            reverse=True
        )

        top10 = sorted_data[:10]

        position = 1

        for item in top10:
            item["position"] = position
            position += 1

        return Response(top10)









############## ATTENDANCE ##################################

class TakeAttendance(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data.copy()

        data['school'] = request.user.school.id

        serializer = AttendanceSerializer(data=data)

        if serializer.is_valid():

            serializer.save()

            return Response({
                "message": "Attendance saved",
                "data": serializer.data
            })

        return Response(serializer.errors)


# Bulk Attendance (VERY IMPORTANT)

# Walimu wengi watachukua attendance ya darasa zima kwa wakati mmoja.

class BulkAttendance(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        attendance_list = request.data

        for item in attendance_list:

            Attendance.objects.update_or_create(
                student_id=item["student"],
                date=item["date"],
                defaults={
                    "school": request.user.school,
                    "classroom_id": item["classroom"],
                    "stream_id": item["stream"],
                    "status": item["status"]
                }
            )

        return Response({
            "message": "Attendance recorded successfully"
        })


##############Get Attendance By Date

class GetAttendanceByDate(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, class_id, date):

        attendance = Attendance.objects.filter(
            classroom_id=class_id,
            date=date,
            school=request.user.school
        )

        serializer = AttendanceSerializer(attendance, many=True)

        return Response(serializer.data)


########### Student Attendance History

class StudentAttendanceHistory(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, student_id):

        attendance = Attendance.objects.filter(
            student_id=student_id,
            school=request.user.school
        ).order_by("-date")

        serializer = AttendanceSerializer(attendance, many=True)

        return Response(serializer.data)



# Attendance Statistics API

# Hii inaonyesha:

# days present

# days absent

class AttendanceStatistics(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, student_id):

        present = Attendance.objects.filter(
            student_id=student_id,
            status='present',
            school=request.user.school
        ).count()

        absent = Attendance.objects.filter(
            student_id=student_id,
            status='absent',
            school=request.user.school
        ).count()

        return Response({
            "present_days": present,
            "absent_days": absent
        })




# views.py (ADD PROMOTION SYSTEM – FULL CODE)
# Promote Single Student

class PromoteStudent(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = StudentPromotionSerializer(data=request.data)

        if serializer.is_valid():

            student_id = serializer.validated_data["student"]
            classroom_id = serializer.validated_data["new_classroom"]
            stream_id = serializer.validated_data["new_stream"]

            student = Student.objects.get(id=student_id)

            student.classroom_id = classroom_id
            student.stream_id = stream_id

            student.save()

            return Response({
                "message": "Student promoted successfully"
            })

        return Response(serializer.errors)


# Promote Whole Class

class PromoteClass(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        class_id = request.data.get("classroom")
        new_class = request.data.get("new_classroom")

        students = Student.objects.filter(
            classroom_id=class_id,
            school=request.user.school
        )

        for student in students:

            student.classroom_id = new_class
            student.save()

        return Response({
            "message": "Class promoted successfully"
        })






# Parent Portal APIs
# Get Children of Parent

class ParentChildren(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        children = Student.objects.filter(
            parent=request.user
        )

        serializer = StudentSerializer(children, many=True)

        return Response(serializer.data)


####  Parent View Child Results

class ParentChildResults(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, student_id):

        student = Student.objects.get(
            id=student_id,
            parent=request.user
        )

        results = Result.objects.filter(student=student)

        serializer = ResultSerializer(results, many=True)

        return Response(serializer.data)



# Report Card Data API (For PDF)

# API hii inatoa data kamili ya report card.

class ReportCardData(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, student_id, exam_id):

        student = Student.objects.get(id=student_id)

        results = Result.objects.filter(
            student_id=student_id,
            exam_id=exam_id
        )

        subjects = []
        total = 0
        count = 0

        for r in results:

            subjects.append({
                "subject": r.subject.name,
                "marks": r.marks
            })

            total += r.marks
            count += 1

        average = total / count if count > 0 else 0

        return Response({

            "student_name": f"{student.first_name} {student.last_name}",

            "classroom": student.classroom.name,

            "stream": student.stream.name,

            "subjects": subjects,

            "total": total,

            "average": average

        })







# views.py (TEACHER MANAGEMENT APIs)
# Create Teacher

class CreateTeacher(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = TeacherSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

###  Get Teachers

class GetTeachers(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        teachers = Teacher.objects.filter(
            school=request.user.school
        )

        serializer = TeacherSerializer(teachers, many=True)

        return Response(serializer.data)


# Fee Structure APIs
# Create Fee Structure

class CreateFeeStructure(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data.copy()

        data['school'] = request.user.school.id

        serializer = FeeStructureSerializer(data=data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)


# Get Fee Structure

class GetFeeStructure(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        fees = FeeStructure.objects.filter(
            school=request.user.school
        )

        serializer = FeeStructureSerializer(fees, many=True)

        return Response(serializer.data)


# Fee Payment APIs
# Pay Fee

class PayFee(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data.copy()

        data['school'] = request.user.school.id

        serializer = FeePaymentSerializer(data=data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)


####  Student Fee History

class StudentFeeHistory(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, student_id):

        payments = FeePayment.objects.filter(
            student_id=student_id,
            school=request.user.school
        )

        serializer = FeePaymentSerializer(payments, many=True)

        return Response(serializer.data)

# Dashboard Analytics APIs

# API hizi zinaonyesha statistics za shule.

# School Dashboard

class SchoolDashboard(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        total_students = Student.objects.filter(
            school=request.user.school
        ).count()

        total_teachers = Teacher.objects.filter(
            school=request.user.school
        ).count()

        total_classes = ClassRoom.objects.filter(
            school=request.user.school
        ).count()

        total_subjects = Subject.objects.filter(
            school=request.user.school
        ).count()

        return Response({

            "total_students": total_students,

            "total_teachers": total_teachers,

            "total_classes": total_classes,

            "total_subjects": total_subjects

        })


# Fee Dashboard

class FeeDashboard(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        total_payments = FeePayment.objects.filter(
            school=request.user.school
        )

        total_amount = sum(
            payment.amount_paid for payment in total_payments
        )

        return Response({

            "total_collected": total_amount,

            "total_transactions": total_payments.count()

        })








# views.py (TIMETABLE APIs)
# Create Timetable

class CreateTimetable(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data.copy()

        data['school'] = request.user.school.id

        serializer = TimetableSerializer(data=data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

# Get Class Timetable

class ClassTimetable(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, class_id):

        timetable = Timetable.objects.filter(
            classroom_id=class_id,
            school=request.user.school
        )

        serializer = TimetableSerializer(timetable, many=True)

        return Response(serializer.data)





###########################################

class GenerateReportCard(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, student_id):

        student = Student.objects.get(id=student_id)

        results = Result.objects.filter(student=student)

        response = HttpResponse(content_type='application/pdf')

        response['Content-Disposition'] = 'attachment; filename="report.pdf"'

        p = canvas.Canvas(response)

        p.drawString(100, 800, "Student Report Card")

        p.drawString(100, 770, f"Student: {student.user.username}")

        y = 730

        for result in results:

            grade = get_grade(result.score, request.user.school)

            text = f"{result.subject.name} : {result.score} ({grade})"

            p.drawString(100, y, text)

            y -= 30

        p.showPage()

        p.save()

        return response