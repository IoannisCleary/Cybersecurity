# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '__first__'),
        ('trainingPortal', '0009_auto_20150311_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='quiz',
            field=models.ForeignKey(default=None, blank=True, to='quiz.Quiz', null=True),
            preserve_default=True,
        ),
    ]
