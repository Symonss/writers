from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ..decorators import admin_required, client_required

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def index(request):

    return render(request, 'coreapp/home.html')

def home(request):
    if request.user.is_authenticated:
        if request.user.is_client:
            return redirect('index')
        elif request.user.is_admin:
                return redirect('index')
        elif request.user.is_sub_admin:
                return redirect('index')
        else:
            return redirect('index')
    return render(request, 'coreapp/home.html')
