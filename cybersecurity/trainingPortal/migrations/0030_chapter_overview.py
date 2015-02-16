# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0029_auto_20150212_0140'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='overview',
            field=models.CharField(default=b'Not available', max_length=500),
            preserve_default=True,
        ),
    ]
