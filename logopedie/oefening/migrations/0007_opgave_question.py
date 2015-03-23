# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oefening', '0006_auto_20150314_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='opgave',
            name='question',
            field=models.CharField(default=b'Klik op het juiste antwoord', max_length=256),
            preserve_default=True,
        ),
    ]
