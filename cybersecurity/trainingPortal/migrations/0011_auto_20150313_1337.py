# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '__first__'),
        ('trainingPortal', '0010_chapter_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='quiz',
        ),
        migrations.AddField(
            model_name='chapter',
            name='quiz_category',
            field=models.ForeignKey(default=None, blank=True, to='quiz.Category', null=True),
            preserve_default=True,
        ),
    ]
