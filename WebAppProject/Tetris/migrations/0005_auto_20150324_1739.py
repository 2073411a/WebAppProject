# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Tetris', '0004_leaderboard_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leaderboard',
            options={'get_latest_by': 'creation_date'},
        ),
        migrations.AddField(
            model_name='leaderboard',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 24, 17, 39, 16, 594251, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
