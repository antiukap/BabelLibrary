# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-31 23:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='learning_langs',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='native_lang',
        ),
    ]
