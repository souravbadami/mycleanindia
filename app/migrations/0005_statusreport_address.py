# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-12 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20161211_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusreport',
            name='address',
            field=models.CharField(default='Unknown', max_length=200),
        ),
    ]
