from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, FormView
from accounts import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
# Create your views here.

class SignUp(CreateView):
    template_name = 'accounts/signup.html'
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:personal_info')

class PersonalInfoView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('accounts:login')
    template_name = 'accounts/personal_info_form.html'
    form_class = forms.PersonalInfoForm
    success_url = reverse_lazy('home')
    registered = False

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    