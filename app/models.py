from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Verycode(models.Model):
    tel = models.CharField(max_length=11,unique=True)
    code = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'verycode'

class User(AbstractUser):
    tel = models.CharField(max_length=11,unique=True)
    class Meta:
        db_table = 'user'