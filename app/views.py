# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import User, Tender

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def dashboard(request, user_id):
    # tenders = get_object_or_404( , pk = user_id)
    tenders = Tender.objects.values('name').filter(pk = User.objects.value_list('tender_categories'))
    # tenders = "\n".join([t.name for t in User.tender_categories.all()])
    print tenders
    context = {'user_id': user_id, 'tenders': tenders}
    return render(request, 'app/dashboard.html', context)

    