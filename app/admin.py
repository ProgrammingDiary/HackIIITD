# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User, Tender, TenderBind
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_tenders')

    def get_tenders(self, obj):
        return "\n".join([t.name for t in obj.tender_categories.all()])

admin.site.register(User, UserAdmin)
admin.site.register(Tender)
admin.site.register(TenderBind)