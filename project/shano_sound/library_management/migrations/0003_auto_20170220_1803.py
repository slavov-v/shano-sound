# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_management', '0002_song_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_file',
            field=models.FileField(upload_to='mymusic'),
        ),
    ]