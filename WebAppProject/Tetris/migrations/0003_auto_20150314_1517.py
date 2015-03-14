# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Tetris', '0002_auto_20150309_2223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='leaderboard',
        ),
        migrations.RemoveField(
            model_name='score',
            name='user',
        ),
        migrations.AddField(
            model_name='score',
            name='iid',
            field=models.CharField(default=datetime.datetime(2015, 3, 14, 15, 17, 5, 724016, tzinfo=utc), unique=True, max_length=256),
            preserve_default=False,
        ),
    ]
