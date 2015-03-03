# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0004_exercise_furtherreadingmode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='question',
            field=models.CharField(default=b'(Empty)', max_length=150),
        ),
    ]
