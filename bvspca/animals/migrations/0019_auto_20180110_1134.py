# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-10 18:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0018_auto_20180105_1128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animalcountsettings',
            options={'verbose_name': 'animals counts'},
        ),
    ]
