# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-05-25 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('psd', models.CharField(max_length=15)),
            ],
        ),
    ]