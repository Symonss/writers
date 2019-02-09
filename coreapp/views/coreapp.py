from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from ..forms import OrderForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ..decorators import admin_required, client_required

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_client:
            return redirect('clients:clients_dashboard')
        elif request.user.is_admin:
                return redirect('admins:admins_dashboard')
        elif request.user.is_sub_admin:
                return redirect('sub_admins:sub_admins_dashboard')
        else:
            return redirect('writers:writers_dashboard')
    return render(request, 'coreapp/home.html')
