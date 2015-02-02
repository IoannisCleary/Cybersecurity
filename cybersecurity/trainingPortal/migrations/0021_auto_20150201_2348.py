# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0020_auto_20150201_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='entry_Activist_Type',
            field=ckeditor.fields.RichTextField(help_text=b'This field is displayed when learningStyleMode is enabled. Activist specific content'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='entry_Pragmatist_Type',
            field=ckeditor.fields.RichTextField(help_text=b'This field is displayed when learningStyleMode is enabled. Pragmatist specific content'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='entry_Reflector_Type',
            field=ckeditor.fields.RichTextField(help_text=b'This field is displayed when learningStyleMode is enabled. Reflector specific content'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='entry_Theorist_Type',
            field=ckeditor.fields.RichTextField(help_text=b'This field is displayed when learningStyleMode is enabled. Theorist specific content'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='learningStyleMode',
            field=models.BooleanField(default=True, help_text=b'Select to enable Learning Style Mode based on Honey & Mumfords learning styles and use the entry fields below. Disable to use default entry field above'),
            preserve_default=True,
        ),
    ]
