from django.shortcuts import render
#from .models import Order

def home_page(request):
    return render(request, 'coreapp/home_page.html', {})

def my_dashboard(request):

    return render(request, 'coreapp/my_dashboard.html', {})
