# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trainingPortal', '0018_auto_20150320_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(default=1, help_text=b'This field is used to sort the sections. Use a unique number', validators=[django.core.validators.MinValueValidator(1)])),
                ('title', models.CharField(max_length=256)),
                ('entry_default', ckeditor.fields.RichTextField(default=b'Empty', help_text=b'This field is displayed when learningStyleMode is disabled.')),
                ('learningStyleMode', models.BooleanField(default=True, help_text=b'Select to enable Learning Style Mode based on Honey & Mumfords learning styles and use the entry fields below. Disable to use default entry field above')),
                ('entry_Activist_Type', ckeditor.fields.RichTextField(default=b'Empty', help_text=b'This field is displayed when learningStyleMode is enabled. Activist specific content')),
                ('entry_Reflector_Type', ckeditor.fields.RichTextField(default=b'Empty', help_text=b'This field is displayed when learningStyleMode is enabled. Reflector specific content')),
                ('entry_Theorist_Type', ckeditor.fields.RichTextField(default=b'Empty', help_text=b'This field is displayed when learningStyleMode is enabled. Theorist specific content')),
                ('entry_Pragmatist_Type', ckeditor.fields.RichTextField(default=b'Empty', help_text=b'This field is displayed when learningStyleMode is enabled. Pragmatist specific content')),
                ('chapter', models.ForeignKey(to='trainingPortal.Chapter')),
            ],
            options={
                'verbose_name_plural': 'Sections',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SectionExercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chapter', models.ForeignKey(to='trainingPortal.Chapter')),
                ('exercise_Activist_id', models.ForeignKey(related_name='exercise_Activist', to='trainingPortal.Exercise')),
                ('exercise_Default_id', models.ForeignKey(related_name='exercise_Default', to='trainingPortal.Exercise')),
                ('exercise_Pragmatist_id', models.ForeignKey(related_name='exercise_Pragmatist', to='trainingPortal.Exercise')),
                ('exercise_Reflector_id', models.ForeignKey(related_name='exercise_Reflector', to='trainingPortal.Exercise')),
                ('exercise_Theorist_id', models.ForeignKey(related_name='exercise_Theorist', to='trainingPortal.Exercise')),
                ('section', models.ForeignKey(to='trainingPortal.Section')),
            ],
            options={
                'verbose_name_plural': 'SectionExercises',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='page',
            name='chapter',
        ),
        migrations.AlterUniqueTogether(
            name='pageexercise',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='pageexercise',
            name='chapter',
        ),
        migrations.RemoveField(
            model_name='pageexercise',
            name='exercise_Activist_id',
        ),
        migrations.RemoveField(
            model_name='pageexercise',
            name='exercise_Default_id',
        ),
        migrations.RemoveField(
            model_name='pageexercise',
            name='exercise_Pragmatist_id',
        ),
        migrations.RemoveField(
            model_name='pageexercise',
            name='exercise_Reflector_id',
        ),
        migrations.RemoveField(
            model_name='pageexercise',
            name='exercise_Theorist_id',
        ),
        migrations.RemoveField(
            model_name='pageexercise',
            name='page',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.DeleteModel(
            name='PageExercise',
        ),
        migrations.AlterUniqueTogether(
            name='sectionexercise',
            unique_together=set([('chapter', 'section')]),
        ),
        migrations.AlterUniqueTogether(
            name='section',
            unique_together=set([('chapter', 'number')]),
        ),
    ]
