# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0012_announcement_indexelement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='entry',
            field=models.CharField(max_length=250),
            preserve_default=True,
        ),
    ]
