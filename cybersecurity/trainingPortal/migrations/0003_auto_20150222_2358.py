# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0002_auto_20150222_2356'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([('chapter', 'number')]),
        ),
    ]
