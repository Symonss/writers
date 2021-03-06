from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.utils import timezone
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from ..decorators import admin_required, client_required
from ..forms import AdminSignUpForm
from ..models import User, Order,User

class AdminSignUpView(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admins'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('admins:admins_dashboard')


@method_decorator([login_required, admin_required], name='dispatch')
class AdminDashboardView(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'coreapp/admins/my_dashboard.html'

@method_decorator([login_required, admin_required], name='dispatch')
class ViewWritersView(ListView):
    model = User
    context_object_name = 'writers'
    template_name = 'coreapp/admins/viewWriters.html'
    # def get_queryset(self):
    #
    #     return queryset

# @method_decorator([login_required, admin_required], name='dispatch')
# class OrderCreateView(CreateView):
#     model=Order
#     fields = ('order_topic', 'order_description', 'pages','track_number','date_created' )
#     template_name = 'coreapp/admins/order_creat_view.html'


# @method_decorator([login_required, client_required], name='dispatch')
# class OrderCreateView(CreateView):
#     form_class= Order
#     template_name = 'coreapp/admins/order_form.html'
#
#     # fields = ['price','deadline', 'words', 'order_topic', 'order_description', 'pages']
