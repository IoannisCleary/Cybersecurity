# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0011_auto_20150201_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='learningStyleDetermined',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='type',
        ),
    ]
