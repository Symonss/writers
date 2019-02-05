from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from coreapp.models import  (User, Client, Admin, SubAdmin)

class WriterSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ('first_name', 'last_name', 'phone','email', )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_writer = True
        if commit:
            user.save()
        return user

class ClientSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ('first_name', 'last_name', 'phone','email', )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        client = Client.objects.create(user=user)
        return user

class SubAdminSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ('first_name', 'last_name', 'phone','email', )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_sub_admin = True
        user.save()
        client = Client.objects.create(user=user)
        return user

class AdminSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ('first_name', 'last_name', 'phone','email', )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.save()
        admin = Admin.objects.create(user=user)
        return user
