# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-31 23:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('bio', models.TextField(blank=True)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('friends', models.ManyToManyField(to='user_manager.Profile')),
                ('learning_langs', models.ManyToManyField(related_name='learners', to='user_manager.Language')),
                ('native_lang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='native_speakers', to='user_manager.Language')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]