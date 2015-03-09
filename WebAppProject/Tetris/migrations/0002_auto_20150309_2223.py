# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Tetris', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='seed',
        ),
        migrations.AddField(
            model_name='score',
            name='leaderboard',
            field=models.ForeignKey(default=datetime.datetime(2015, 3, 9, 22, 23, 33, 708965, tzinfo=utc), to='Tetris.Leaderboard'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='score',
            name='user',
            field=models.ForeignKey(to='Tetris.UserProfile'),
            preserve_default=True,
        ),
    ]
