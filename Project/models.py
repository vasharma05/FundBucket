from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name


class Project(models.Model):
    author = models.ForeignKey(auth.User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    title = models.CharField(max_length=255, required = True)
    description = models.TextField(required = True, required = True)
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish_project(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return title

class Funds(models.Model)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    funds_collected = models.IntegerField(default=0)
    target_funds = models.IntegerField(required = True)

    def add_funds(self, value):
        self.funds_collected += target_funds
        self.save()
    
    def update_target_funds(self, value):
        self.target_funds = value
        self.save()

    def deduct_funds(seld, value):
        if self.funds_collected >= value:
            funds_collected -= value
            return True
        else:
            return False


