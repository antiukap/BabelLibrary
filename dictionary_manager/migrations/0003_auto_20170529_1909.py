# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-29 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary_manager', '0002_auto_20170529_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='definitions',
            name='additional_information',
            field=models.TextField(null=True),
        ),
    ]