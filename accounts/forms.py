from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, get_user_model
from accounts import models
#Accounts Forms

class UserCreateForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class PersonalInfoForm(forms.ModelForm):
    class Meta():
        model = models.PersonalInfo
        fields = "__all__"