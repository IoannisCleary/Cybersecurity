# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0003_auto_20150302_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='furtherReadingMode',
            field=models.BooleanField(default=False, help_text=b'Select to use only the text field without the answer fields.'),
            preserve_default=True,
        ),
    ]
