# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0025_auto_20150212_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testing',
            name='mode',
            field=models.BooleanField(default=False, help_text=b'Select to enable Testing Mode where type A users see only default parts of chapters and type B users see learning style specific parts of chapters'),
            preserve_default=True,
        ),
    ]
