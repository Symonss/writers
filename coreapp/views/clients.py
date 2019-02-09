from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from ..decorators import client_required
from ..forms import ClientSignUpForm
from ..models import Client, User, Order

class ClientSignUpView(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('clients:clients_dashboard')

@method_decorator([login_required, client_required], name='dispatch')
class ClientDashboardView(ListView):
    model = Client
    context_object_name = 'clients_dashboard'
    template_name = 'coreapp/clients/my_dashboard.html'

    def my_dashboard(request):
        return render(request, 'coreapp/clients/my_dashboard.html', {})


class OrderCreate(CreateView):
    model = Order
    fields = '__all__'
    success_url = reverse_lazy('home')

    # initial = {'date_of_death': '05/01/2018'}

class OrderUpdate(UpdateView):
    model = Order
    fields = ['pages']

class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('home')
