from django.contrib import admin
from .models import *

admin.site.register(School)
admin.site.register(CustomerUser)
admin.site.register(ClassRoom)
admin.site.register(Stream)
admin.site.register(Subject)
admin.site.register(Student)

##########################################

admin.site.register(ExamCategory)
admin.site.register(Exam)
admin.site.register(Result)


######################################
admin.site.register(Attendance)


#######################################

admin.site.register(Teacher)
admin.site.register(FeeStructure)
admin.site.register(FeePayment)


#################################
admin.site.register(Timetable)
admin.site.register(GradingSystem)