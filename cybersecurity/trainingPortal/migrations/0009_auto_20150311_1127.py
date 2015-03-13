# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0008_auto_20150311_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='overview',
            field=ckeditor.fields.RichTextField(default=b'Not available', help_text=b'This field displays the correct answer and the explanation why. If multipleMode is enabled it will display all the correct answers from the exercises above. (Remember to add a number to each exercise)'),
            preserve_default=True,
        ),
    ]
