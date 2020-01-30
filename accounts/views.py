from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from accounts import forms
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class SignUp(CreateView):
    template_name = 'accounts/signup.html'
    form_class = forms.UserCreateForm
    success_url = 'personal_info'

class PersonalInfoView(CreateView, LoginRequiredMixin):
    login_url = 'accounts:login'
    template_name = 'accounts/personal_info_form.html'
    form_class = forms.PersonalInfoForm
