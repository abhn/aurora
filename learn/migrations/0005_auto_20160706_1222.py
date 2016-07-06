# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0004_qualityfeedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('feedback_email', models.CharField(default=b'Anon', max_length=100)),
                ('feedback_name', models.CharField(default=b'Anon', max_length=100)),
                ('feedback_msg', models.TextField(null=True, blank=True)),
                ('feedback_extra', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['feedback'],
                'db_table': 'feedback_data',
            },
        ),
        migrations.CreateModel(
            name='FeedbackInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('feedback', models.CharField(unique=True, max_length=100)),
                ('feedback_type', models.IntegerField(default=999)),
                ('feedback_desc', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['feedback_type'],
                'db_table': 'feedback_types',
            },
        ),
        migrations.AddField(
            model_name='feedbackdata',
            name='feedback',
            field=models.ForeignKey(to='learn.FeedbackInfo'),
        ),
    ]
