# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0005_auto_20150302_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='disableMode',
            field=models.BooleanField(default=False, help_text=b"If you don't want this exercise to appear or to make it an empty option"),
            preserve_default=True,
        ),
    ]
