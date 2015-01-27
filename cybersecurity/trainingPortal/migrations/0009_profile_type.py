# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0008_auto_20150125_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='type',
            field=models.CharField(default=b'not selected', max_length=128),
            preserve_default=True,
        ),
    ]
