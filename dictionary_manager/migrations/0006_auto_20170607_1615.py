# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-07 13:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0004_auto_20170607_1615'),
        ('dictionary_manager', '0005_auto_20170529_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translation', models.TextField()),
                ('translation_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_manager.Language')),
            ],
        ),
        migrations.AddField(
            model_name='word',
            name='translations',
            field=models.ManyToManyField(to='dictionary_manager.Translation'),
        ),
    ]
