# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-17 17:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20180216_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialmediaqueue',
            name='ready',
        ),
    ]