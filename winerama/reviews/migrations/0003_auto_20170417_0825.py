# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 08:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_cliuster'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cliuster',
            new_name='Cluster',
        ),
    ]
