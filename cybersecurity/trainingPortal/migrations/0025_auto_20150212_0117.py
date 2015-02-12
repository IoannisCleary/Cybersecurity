# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0024_auto_20150212_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='number',
            field=models.IntegerField(default=0, help_text=b'This field is used to sort the chapters. Use a unique number'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='number',
            field=models.IntegerField(default=0, help_text=b'This field is used to sort the pages. Use a unique number'),
            preserve_default=True,
        ),
    ]
