from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from ..decorators import sub_admin_required
from ..forms import SubAdminSignUpForm
from ..models import User

class SubAdminSignUpView(CreateView):
    model = User
    form_class = SubAdminSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'writers'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('sub_admins:sub_admins_dashboard')


class SubAdminDashboardView(ListView):
    model = User
    context_object_name = 'sub_admins_dashboard'
    template_name = 'coreapp/sub_admin/my_dashboard.html'

    def my_dashboard(request):
        return render(request, 'coreapp/sub_admin/my_dashboard.html', {})
