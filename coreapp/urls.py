# from django.urls import path
# from . import views
from django.conf import settings
from django.conf.urls.static import static
#
# urlpatterns = [
#     path('', views.home_page, name='home_page'),
#     path('mydashboard', views.my_dashboard, name='my_dashboard'),
# ]

from django.urls import include, path

from .views import coreapp, clients, admins, writers, sub_admin

urlpatterns = [
    path('', coreapp.index, name='index'),
    path('home', coreapp.home, name='home'),
    
    # path('create', coreapp.create_order, name='create_order'),
    

    path('clients/', include(([
        path('order/create/', clients.OrderCreate.as_view(), name='order_create'),
        path('form/upload/', clients.model_form_upload, name= 'upload'),
        path('dashboard', clients.ClientDashboardView.as_view(), name='clients_dashboard'),
        path('order/<int:pk>/update/', clients.OrderUpdate.as_view(), name='order_update'),
        path('order/<int:pk>/delete/', clients.OrderDelete.as_view(), name='order_delete'),

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
        path('writers', admins.ViewWritersView.as_view(), name='writers'),
        # path('create', admins.OrderCreateView.as_view(), name='create_order'),
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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)