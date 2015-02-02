# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0015_auto_20150201_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='entry_Activist_Type',
            field=ckeditor.fields.RichTextField(),
            preserve_default=True,
        ),
    ]
