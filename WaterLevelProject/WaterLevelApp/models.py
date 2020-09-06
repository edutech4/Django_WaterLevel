from django.db import models

#Create your models here.


class Device(models.Model):
    device_id = models.CharField(max_length=128)
    tank_height = models.BigIntegerField(max_length=128)
    location = models.CharField(max_length=128)
    user_id = models.BigIntegerField(max_length=128)


class User(models.Model):
    Username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    phone = models.BigIntegerField(max_length=128)

