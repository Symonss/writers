from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('mydashboard', views.my_dashboard, name='my_dashboard'),
]
