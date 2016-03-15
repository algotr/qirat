# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funeral', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funeral',
            old_name='added_by',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='funeral',
            old_name='added_at',
            new_name='create_date',
        ),
        migrations.RemoveField(
            model_name='funeral',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='funeral',
            name='updated_by',
        ),
        migrations.AddField(
            model_name='funeral',
            name='name',
            field=models.CharField(default='no name', max_length=250),
            preserve_default=False,
        ),
    ]
