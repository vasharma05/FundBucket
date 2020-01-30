from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserModel(User):

   def __str__(self):
       return "@{}".format(self.username)

class PersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    roll_no = models.CharField(max_length=10, primary_key=True)
    department = models.CharField(max_length= 100)
    mobile_number = models.IntegerField()
    profile_pic = models.FileField()

