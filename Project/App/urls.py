from django.urls import path
from . import views

urlpatterns = [
    path('LatestVersionView/', views.LatestVersionView.as_view(), name='LatestVersionView'),

    path('register/', views.RegisterUser.as_view()),

    path('login/', views.LoginUser.as_view()),

    path('create-school/', views.CreateSchool.as_view()),

    path('create-class/', views.CreateClassRoom.as_view()),

    path('classes/', views.GetClasses.as_view()),

    path('create-stream/', views.CreateStream.as_view()),

    path('streams/<int:class_id>/', views.GetStreams.as_view()),

    path('create-student/', views.CreateStudent.as_view()),

    path('students/', views.GetStudents.as_view()),

    path("parents/", views.GetParents.as_view()),

    path('students/stream/<int:stream_id>/', views.GetStudentsInStream.as_view()),
    



    ##########################################################

    path('create-subject/', views.CreateSubject.as_view()),

    path('subjects/', views.GetSubjects.as_view()),

    path('create-exam-category/', views.CreateExamCategory.as_view()),

    path('exam-categories/', views.GetExamCategories.as_view()),

    path('create-exam/', views.CreateExam.as_view()),

    path('exams/', views.GetExams.as_view()),

    path('add-result/', views.AddResult.as_view()),

    path('bulk-results/', views.BulkResultUpload.as_view()),

    path('student-results/<int:student_id>/', views.GetStudentResults.as_view()),

    path('exam-results/<int:exam_id>/', views.GetExamResults.as_view()),



    ####################################################################

        path(
        'report-card/<int:student_id>/<int:exam_id>/',
        views.StudentReportCard.as_view()
    ),

    path(
        'class-ranking/<int:class_id>/<int:exam_id>/',
        views.ClassRanking.as_view()
    ),

    path(
        'stream-ranking/<int:stream_id>/<int:exam_id>/',
        views.StreamRanking.as_view()
    ),

    path(
        'top10/<int:class_id>/<int:exam_id>/',
        views.TopStudents.as_view()
    ),




    ######################### ATTENDANCE ##########################

        path(
        'take-attendance/',
        views.TakeAttendance.as_view()
    ),

    path(
        'bulk-attendance/',
        views.BulkAttendance.as_view()
    ),

    path(
        'attendance/<int:class_id>/<str:date>/',
        views.GetAttendanceByDate.as_view()
    ),

    path(
        'student-attendance/<int:student_id>/',
        views.StudentAttendanceHistory.as_view()
    ),

    path(
        'attendance-statistics/<int:student_id>/',
        views.AttendanceStatistics.as_view()
    ),







    #############################################################


        path(
        'promote-student/',
        views.PromoteStudent.as_view()
    ),

    path(
        'promote-class/',
        views.PromoteClass.as_view()
    ),

    path(
        'parent-children/',
        views.ParentChildren.as_view()
    ),

    path(
        'parent-child-results/<int:student_id>/',
        views.ParentChildResults.as_view()
    ),

    path(
        'report-card-data/<int:student_id>/<int:exam_id>/',
        views.ReportCardData.as_view()
    ),






    ##########################################################

        path(
        'create-teacher/',
        views.CreateTeacher.as_view()
    ),

    path(
        'teachers/',
        views.GetTeachers.as_view()
    ),

    path(
        'create-fee-structure/',
        views.CreateFeeStructure.as_view()
    ),

    path(
        'fee-structure/',
        views.GetFeeStructure.as_view()
    ),

    path(
        'pay-fee/',
        views.PayFee.as_view()
    ),

    path(
        'student-fee-history/<int:student_id>/',
        views.StudentFeeHistory.as_view()
    ),

    path(
        'school-dashboard/',
        views.SchoolDashboard.as_view()
    ),

    path(
        'fee-dashboard/',
        views.FeeDashboard.as_view()
    ),





    ##########################################################

        path(
        'create-timetable/',
        views.CreateTimetable.as_view()
    ),

    path(
        'class-timetable/<int:class_id>/',
        views.ClassTimetable.as_view()
    ),

    path(
        'generate-report/<int:student_id>/',
        views.GenerateReportCard.as_view()
    ),

]

#CreateResult