# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0013_remove_profile_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='entry',
        ),
        migrations.AddField(
            model_name='page',
            name='entry_Activist_Type',
            field=ckeditor.fields.RichTextField(default=b'This field is displayed when learningStyleMode is True. Activist specific content'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='entry_Pragmatist_Type',
            field=ckeditor.fields.RichTextField(default=b'This field is displayed when learningStyleMode is True. Pragmatist specific content'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='entry_Reflector_Type',
            field=ckeditor.fields.RichTextField(default=b'This field is displayed when learningStyleMode is True. Reflector specific content'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='entry_Theorist_Type',
            field=ckeditor.fields.RichTextField(default=b'This field is displayed when learningStyleMode is True. Theorist specific content'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='entry_default',
            field=ckeditor.fields.RichTextField(default=b'This field is displayed when learningStyleMode is False.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='learningStyleMode',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
