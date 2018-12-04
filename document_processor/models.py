from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    user = models.ForeignKey(User, related_name='user_address', on_delete=models.CASCADE)
    address = models.CharField(max_length=64, blank=True)
    vat_no = models.CharField(max_length=32, blank=True)
    tel_no = models.CharField(max_length=16, blank=True)


class Billed(models.Model):

    address = models.CharField(max_length=64, blank=True)
    acc_no = models.CharField(max_length=32, blank=True)
    name = models.CharField(max_length=64, blank=True) 

class Item(models.Model):

    name = models.CharField(max_length=64)
    cost = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=7)