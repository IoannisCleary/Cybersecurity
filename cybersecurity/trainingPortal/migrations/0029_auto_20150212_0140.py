# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0028_auto_20150212_0137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mode',
            old_name='mode',
            new_name='enable',
        ),
    ]
