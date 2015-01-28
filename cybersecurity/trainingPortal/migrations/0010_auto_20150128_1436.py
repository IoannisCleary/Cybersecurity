# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0009_profile_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='learningStyleDetermined',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='learningType',
            field=models.CharField(default=b'not determined', max_length=60),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='type',
            field=models.CharField(default=b'not selected', max_length=2),
            preserve_default=True,
        ),
    ]
