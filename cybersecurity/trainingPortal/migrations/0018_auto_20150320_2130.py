# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0017_auto_20150316_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='number',
            field=models.IntegerField(default=1, help_text=b'This field is used to sort the sections. Use a unique number', validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=True,
        ),
    ]
