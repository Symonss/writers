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

from ..decorators import writer_required
from ..forms import WriterSignUpForm
from ..models import User

class WriterSignUpView(CreateView):
    model = User
    form_class = WriterSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'writers'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('writers:writers_dashboard')

@method_decorator([login_required, writer_required], name='dispatch')
class WriterDashboardView(ListView):
    model = User
    context_object_name = 'writers_dashboard'
    template_name = 'coreapp/writers/my_dashboard.html'

    def my_dashboard(request):
        return render(request, 'coreapp/writers/my_dashboard.html', {})
