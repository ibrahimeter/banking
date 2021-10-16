from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserToken(models.Model):
    user = models.ForeignKey(User, models.CASCADE,blank= True, null=True)
    token = models.UUIDField(blank= True, null=True)