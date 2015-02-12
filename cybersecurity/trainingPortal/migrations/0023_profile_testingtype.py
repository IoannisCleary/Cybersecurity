# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0022_auto_20150202_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='testingType',
            field=models.CharField(default=b'0', max_length=1, choices=[(b'0', b'A'), (b'1', b'B')]),
            preserve_default=True,
        ),
    ]
