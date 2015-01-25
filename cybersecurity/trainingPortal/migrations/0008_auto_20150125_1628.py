# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0007_auto_20150125_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='content',
            new_name='entry',
        ),
    ]
