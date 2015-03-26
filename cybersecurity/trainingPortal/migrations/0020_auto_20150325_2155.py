# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0019_auto_20150325_2130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='learningType',
            new_name='learningStyle',
        ),
    ]
