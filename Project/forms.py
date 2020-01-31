from django import forms
from Project.models import (Project, Funds) 

class Project_Form(forms.ModelForm):

    class Meta():
        model = Project
        fields = ('title', 'description', '')