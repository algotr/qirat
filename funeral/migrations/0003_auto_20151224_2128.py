# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funeral', '0002_auto_20151224_1034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funeral',
            options={'ordering': ['-create_date']},
        ),
    ]
