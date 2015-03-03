# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0002_auto_20150302_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='diagram',
            field=filer.fields.image.FilerImageField(related_name=b'exercise_image', blank=True, to='filer.Image', null=True),
        ),
    ]
