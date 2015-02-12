# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0027_auto_20150212_0130'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Modes',
            new_name='Mode',
        ),
    ]
