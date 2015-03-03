# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pageexercise',
            old_name='exercise_Activist',
            new_name='exercise_Activist_id',
        ),
        migrations.RenameField(
            model_name='pageexercise',
            old_name='exercise_Default',
            new_name='exercise_Default_id',
        ),
        migrations.RenameField(
            model_name='pageexercise',
            old_name='exercise_Pragmatist',
            new_name='exercise_Pragmatist_id',
        ),
        migrations.RenameField(
            model_name='pageexercise',
            old_name='exercise_Reflector',
            new_name='exercise_Reflector_id',
        ),
        migrations.RenameField(
            model_name='pageexercise',
            old_name='exercise_Theorist',
            new_name='exercise_Theorist_id',
        ),
    ]
