# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 19:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('metapile', '0002_auto_20161111_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 11, 11, 19, 14, 19, 729951, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
