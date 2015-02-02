# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0016_auto_20150201_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='entry_Activist_Type',
            field=models.TextField(help_text=b'This field is displayed when learningStyleMode is True. Activist specific content'),
            preserve_default=True,
        ),
    ]
