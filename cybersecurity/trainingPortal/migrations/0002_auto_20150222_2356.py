# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='number',
            field=models.IntegerField(default=0, help_text=b'This field is used to sort the chapters. Use a unique number', unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([('chapter', 'title', 'number')]),
        ),
    ]
