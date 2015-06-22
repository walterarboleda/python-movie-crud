# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('MovieLib', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=128, default=datetime.date(2014, 9, 7)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='release_date',
            field=models.DateField(default=datetime.date(2014, 9, 7)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=128, default=0.0004965243296921549),
            preserve_default=False,
        ),
    ]
