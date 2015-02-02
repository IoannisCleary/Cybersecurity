# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0019_auto_20150201_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='entry_default',
            field=ckeditor.fields.RichTextField(help_text=b'This field is displayed when learningStyleMode is disabled.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='learningStyleMode',
            field=models.BooleanField(default=True, help_text=b'Select to enable Learning Style Mode and use the entry fields below. Disable to use default entry field above'),
            preserve_default=True,
        ),
    ]
