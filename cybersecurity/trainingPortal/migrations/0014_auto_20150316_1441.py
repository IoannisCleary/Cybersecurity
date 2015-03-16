# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0013_auto_20150316_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indexelement',
            name='title',
        ),
        migrations.AddField(
            model_name='indexelement',
            name='number',
            field=models.IntegerField(default=1, help_text=b'This field is used to sort the elementss. Use a unique number', validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=True,
        ),
    ]
