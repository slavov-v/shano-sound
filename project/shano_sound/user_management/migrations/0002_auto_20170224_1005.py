# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
