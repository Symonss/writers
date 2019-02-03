from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_client:
            return redirect('clients:clients_dashboard')
        else:
            return redirect('writers:writers_dashboard')
    return render(request, 'coreapp/home.html')
