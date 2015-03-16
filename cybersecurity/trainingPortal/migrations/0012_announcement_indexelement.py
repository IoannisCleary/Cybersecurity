# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0011_auto_20150313_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=128)),
                ('entry', ckeditor.fields.RichTextField(default=b'Empty', help_text=b'This field will be shown on the homepage.')),
            ],
            options={
                'verbose_name_plural': 'Announcements',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IndexElement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Main', unique=True, max_length=128)),
                ('entry', ckeditor.fields.RichTextField(default=b'Empty', help_text=b'This field will be shown on the homepage.')),
            ],
            options={
                'verbose_name_plural': 'IndexElements',
            },
            bases=(models.Model,),
        ),
    ]
