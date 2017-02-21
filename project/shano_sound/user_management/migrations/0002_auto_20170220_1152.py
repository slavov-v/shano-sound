# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import user_management.custom_fields


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=user_management.custom_fields.PasswordModelField(max_length=20),
        ),
    ]
