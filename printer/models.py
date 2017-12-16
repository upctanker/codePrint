from django.db import models

class UserInfo(models.Model):
    team = models.CharField(max_length=100,default="teamtest")
    password = models.CharField(max_length=100,default="")
    seat = models.CharField(max_length=100,default="")
