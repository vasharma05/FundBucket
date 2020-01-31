from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class PersonalInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=10, primary_key=True)
    department = models.CharField(max_length= 100, blank=True)
    profile_pic = models.ImageField(default='https://drive.google.com/open?id=16ZU24pGnhv3UUrdbb6vQSagFGiKHLMWX')
    # registered = models.BooleanField(default=False)
