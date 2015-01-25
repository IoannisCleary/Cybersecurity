# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0003_auto_20150124_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='content',
        ),
    ]
