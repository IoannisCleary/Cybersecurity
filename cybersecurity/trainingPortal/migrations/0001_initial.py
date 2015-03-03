# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import ckeditor.fields
import filer.fields.image
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('filer', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(default=1, help_text=b'This field is used to sort the chapters. Use a unique number', unique=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('title', models.CharField(unique=True, max_length=128)),
                ('overview', models.CharField(default=b'Not available', max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Chapters',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(default=1, help_text=b'This field is used to sort the exercises. Use a unique number', unique=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('question', models.CharField(max_length=150)),
                ('multipleMode', models.BooleanField(default=False, help_text=b'If you want to add multiple exercises enable this and in the text field below add both exercises and the available answers')),
                ('diagramMode', models.BooleanField(default=False, help_text=b'Select to use a diagram instead of text. Used when multipleMode is disabled.')),
                ('text', ckeditor.fields.RichTextField(default=b'Empty', help_text=b'This field is used instead of a diagram to add information about a question. When multipleMode is enabled this field should contain exercises and the available answers.(Remember to add a number to each exercise + add a letter for each answer)')),
                ('source', models.CharField(default=b'No source', help_text=b'This field is used to add source of diagram or question', max_length=200)),
                ('availableAnswers', ckeditor.fields.RichTextField(default=b'Empty', help_text=b'Used only when multipleMode is disabled. This field displays the available answers to this exercise')),
                ('correctAnswer', ckeditor.fields.RichTextField(default=b'Not available', help_text=b'This field displays the correct answer and the explanation why. If multipleMode is enabled it will display all the correct answers from the exercises above. (Remember to add a number to each exercise)')),
                ('chapter', models.ForeignKey(to='trainingPortal.Chapter')),
                ('diagram', filer.fields.image.FilerImageField(related_name=b'exercise_image', to='filer.Image')),
            ],
            options={
                'verbose_name_plural': 'Exercises',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('enable', models.BooleanField(default=False, help_text=b'Select to enable Testing Mode where type A users see only default parts of chapters and type B users see learning style specific parts of chapters')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(default=1, help_text=b'This field is used to sort the pages. Use a unique number', validators=[django.core.validators.MinValueValidator(1)])),
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
                'verbose_name_plural': 'Pages',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageExercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chapter', models.ForeignKey(to='trainingPortal.Chapter')),
                ('exercise_Activist', models.ForeignKey(related_name=b'exercise_Activist', to='trainingPortal.Exercise')),
                ('exercise_Default', models.ForeignKey(related_name=b'exercise_Default', to='trainingPortal.Exercise')),
                ('exercise_Pragmatist', models.ForeignKey(related_name=b'exercise_Pragmatist', to='trainingPortal.Exercise')),
                ('exercise_Reflector', models.ForeignKey(related_name=b'exercise_Reflector', to='trainingPortal.Exercise')),
                ('exercise_Theorist', models.ForeignKey(related_name=b'exercise_Theorist', to='trainingPortal.Exercise')),
                ('page', models.ForeignKey(to='trainingPortal.Page')),
            ],
            options={
                'verbose_name_plural': 'PageExercises',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField()),
                ('learningType', models.CharField(default=b'0', max_length=1, choices=[(b'0', b'Not selected'), (b'1', b'Activist'), (b'2', b'Reflector'), (b'3', b'Theorist'), (b'4', b'Pragmatist')])),
                ('testingType', models.CharField(default=b'0', max_length=1, choices=[(b'0', b'A'), (b'1', b'B')])),
                ('profile_pic', filer.fields.image.FilerImageField(related_name=b'profile_picture', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='filer.Image', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='pageexercise',
            unique_together=set([('chapter', 'page')]),
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([('chapter', 'number')]),
        ),
        migrations.AlterUniqueTogether(
            name='exercise',
            unique_together=set([('chapter', 'number')]),
        ),
    ]
