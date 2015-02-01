# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0010_auto_20150128_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='learningType',
            field=models.CharField(default=b'0', max_length=1, choices=[(b'0', b'Not selected'), (b'1', b'Activist'), (b'2', b'Reflector'), (b'3', b'Theorist'), (b'4', b'Pragmatist')]),
            preserve_default=True,
        ),
    ]
