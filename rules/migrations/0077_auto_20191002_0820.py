# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-10-02 08:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0076_merge_20190926_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraction',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='useraction',
            name='object_id',
        ),
    ]
