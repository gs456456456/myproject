# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-05-27 02:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dairy', '0003_auto_20170527_0212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dairy',
            old_name='date',
            new_name='ddate',
        ),
    ]