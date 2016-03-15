# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funeral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('body', models.TextField()),
                ('house_position', models.CharField(null=True, max_length=200, blank=True)),
                ('mosque_position', models.CharField(null=True, max_length=200, blank=True)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(max_length=200)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('place_tags',
                 taggit.managers.TaggableManager(to='taggit.Tag', verbose_name='Tags', through='taggit.TaggedItem',
                                                 help_text='A comma-separated list of tags.')),
            ],
            options={
                'db_table': 'funeral',
            },
        ),
    ]
