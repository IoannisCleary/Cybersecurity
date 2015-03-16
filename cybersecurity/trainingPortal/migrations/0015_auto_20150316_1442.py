# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0014_auto_20150316_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='number',
            field=models.IntegerField(default=1, help_text=b'This field is used to sort the announcements. Use a unique number', validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='indexelement',
            name='number',
            field=models.IntegerField(default=1, help_text=b'This field is used to sort the elements. Use a unique number', validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=True,
        ),
    ]
