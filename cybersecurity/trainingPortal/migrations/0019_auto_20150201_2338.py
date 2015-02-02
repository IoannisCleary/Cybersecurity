# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0018_auto_20150201_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='learningStyleMode',
            field=models.BooleanField(default=True, help_text=b'Select to enable Learning Style Mode and use the entry fields below. Untick to use default entry field above'),
            preserve_default=True,
        ),
    ]
