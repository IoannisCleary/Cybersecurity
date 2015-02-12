# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0023_profile_testingtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mode', models.BooleanField(default=True, help_text=b'Select to enable Testing Mode where type A users see only default parts of chapters and type B users see learning style specific parts of chapters')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='chapter',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
