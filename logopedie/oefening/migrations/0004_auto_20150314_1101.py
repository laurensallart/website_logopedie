# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oefening', '0003_auto_20150313_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='child',
            name='userName',
            field=models.CharField(default=' ', unique=True, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oefeningenreeks',
            name='slug',
            field=models.SlugField(default='test', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='opgave',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='opgave',
            name='name',
            field=models.CharField(unique=True, max_length=128),
            preserve_default=True,
        ),
    ]
