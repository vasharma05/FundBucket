from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, FormView
from accounts import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from . import models
# Create your views here.

class SignUp(CreateView):
    template_name = 'accounts/signup.html'
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:personal_info')

class PersonalInfoView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('accounts:login')
    template_name = 'accounts/personal_info_form.html'
    form_class = forms.PersonalInfoForm
    success_url = reverse_lazy('projects:post_list')
    registered = False

    def get(self, request):
        if request.user.personal.user:
            return redirect('projects:post_list')
        else:
            form = forms.PersonalInfoForm()
            return render(request, 'accounts/personal_info_form.html', context={'form':form})

    def post(self, request):
        form = forms.PersonalInfoForm(request.POST, request.FILES)
        model = models.PersonalInfo(request.POST, request.FILES)
        if form.is_valid():
            model = form.save(commit=False)
            model.user = request.user
            model.save()
            self.registered = True
            return redirect('projects:post_list')
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     form.instance.profile_pic = self.request.FILES.getlist('profile_pic')
    #     print(form.instance.profile_pic)
    #     # return super().form_valid(form)

    