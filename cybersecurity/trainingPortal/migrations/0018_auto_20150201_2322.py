# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0017_auto_20150201_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='entry_Activist_Type',
            field=ckeditor.fields.RichTextField(help_text=b'This field is displayed when learningStyleMode is True. Activist specific content'),
            preserve_default=True,
        ),
    ]
