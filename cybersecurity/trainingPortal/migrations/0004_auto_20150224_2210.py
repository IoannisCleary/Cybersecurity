# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0003_auto_20150222_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='number',
            field=models.IntegerField(default=1, help_text=b'This field is used to sort the chapters. Use a unique number', unique=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='page',
            name='number',
            field=models.IntegerField(default=1, help_text=b'This field is used to sort the pages. Use a unique number', validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
