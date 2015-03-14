# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tetris', '0003_auto_20150314_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='iid',
        ),
        migrations.AddField(
            model_name='score',
            name='leaderboard',
            field=models.ForeignKey(default='0', to='Tetris.Leaderboard'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='score',
            name='user',
            field=models.ForeignKey(default=0, to='Tetris.UserProfile'),
            preserve_default=False,
        ),
    ]
