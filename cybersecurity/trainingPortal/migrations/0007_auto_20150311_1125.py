# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0006_exercise_disablemode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='overview',
            field=tinymce.models.HTMLField(),
            preserve_default=True,
        ),
    ]
