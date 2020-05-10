from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    #we allow blank fields whihc in the DB will be represented as a blank
    age = models.PositiveIntegerField(null=True,blank=True)

