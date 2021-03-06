# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 23:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_tender_current_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='TenderBind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('binded_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
                ('tenders', models.ManyToManyField(to='app.Tender')),
            ],
        ),
    ]
