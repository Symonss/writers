from django.contrib import admin
from django.urls import path, include
from coreapp.views import coreapp, clients, writers, sub_admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coreapp.urls')), #redirecting urls requests to coreapp.urls
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', coreapp.SignUpView.as_view(), name='signup'),
    path('accounts/signup/client/', clients.ClientSignUpView.as_view(), name='client_signup'),
    path('accounts/signup/writer/', writers.WriterSignUpView.as_view(), name='writer_signup'),
    path('accounts/signup/sub_admin/', sub_admin.SubAdminSignUpView.as_view(), name='sub_admin_signup'),
]
