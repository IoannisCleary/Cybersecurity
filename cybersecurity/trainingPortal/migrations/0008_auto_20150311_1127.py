# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0007_auto_20150311_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='overview',
            field=models.CharField(default=b'Not available', max_length=500),
            preserve_default=True,
        ),
    ]
