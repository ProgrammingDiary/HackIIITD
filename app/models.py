# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms
import datetime
from django.utils import timezone
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    password = models.CharField(max_length = 100)
    number = models.BigIntegerField()
    organisation = models.CharField(max_length = 100)
    tender_categories = models.ManyToManyField('Tender')

    def __unicode__(self):
        return "%s" % (self.tender_categories)

class Tender(models.Model):
    # current_user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 300)
    category = models.CharField(max_length = 200)
    active = models.BooleanField(default = False)
    archived = models.BooleanField(default = False)
    start_date = models.DateField(default = timezone.now)
    end_date = models.DateField(default = timezone.now)

    def __unicode__(self):
        return "%s" % (self.name)

class TenderBind(models.Model):
    binded_to = models.ForeignKey(User, on_delete = models.CASCADE)
    tenders = models.ManyToManyField('Tender')    

    def __unicode__(self):
        return "%s" % (self.binded_to)