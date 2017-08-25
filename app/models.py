# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    password = models.CharField(max_length = 100)
    number = models.IntegerField()
    organisation = models.CharField(max_length = 100)