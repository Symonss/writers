# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.home_page, name='home_page'),
#     path('mydashboard', views.my_dashboard, name='my_dashboard'),
# ]

from django.urls import include, path

from .views import coreapp, clients, admins, writers, sub_admin

urlpatterns = [
    path('', coreapp.home, name='home'),

    path('clients/', include(([
        path('', clients.ClientDashboardView.as_view(), name='clients_dashboard'),
        # path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
        # path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
        # path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
    ], 'coreapp'), namespace='clients')),


    path('Assistant/Admin/', include(([
        path('', sub_admin.SubAdminDashboardView.as_view(), name='sub_admins_dashboard'),
        # path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
        # path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
        # path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
    ], 'coreapp'), namespace='sub_admins')),


    path('Super-Admin/', include(([
        path('', admins.AdminDashboardView.as_view(), name='admins_dashboard'),
        # path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
        # path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
        # path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
    ], 'coreapp'), namespace='admins')),


    path('writers/', include(([
        path('', writers.WriterDashboardView.as_view(), name='writers_dashboard'),
        # path('quiz/add/', teachers.QuizCreateView.as_view(), name='quiz_add'),
        # path('quiz/<int:pk>/', teachers.QuizUpdateView.as_view(), name='quiz_change'),
        # path('quiz/<int:pk>/delete/', teachers.QuizDeleteView.as_view(), name='quiz_delete'),
        # path('quiz/<int:pk>/results/', teachers.QuizResultsView.as_view(), name='quiz_results'),
        # path('quiz/<int:pk>/question/add/', teachers.question_add, name='question_add'),
        # path('quiz/<int:quiz_pk>/question/<int:question_pk>/', teachers.question_change, name='question_change'),
        # path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', teachers.QuestionDeleteView.as_view(), name='question_delete'),
    ], 'coreapp'), namespace='writers')),
]
