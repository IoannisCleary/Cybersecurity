# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapter',
            options={'verbose_name_plural': 'Chapters'},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name_plural': 'Pages'},
        ),
    ]
