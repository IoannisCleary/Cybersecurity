# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0026_auto_20150212_0124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('mode', models.BooleanField(default=False, help_text=b'Select to enable Testing Mode where type A users see only default parts of chapters and type B users see learning style specific parts of chapters')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Testing',
        ),
    ]
