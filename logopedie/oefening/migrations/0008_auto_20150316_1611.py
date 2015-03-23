# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oefening', '0007_opgave_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opgave',
            name='question',
            field=models.CharField(default=b'Klik op het juiste antwoord', max_length=256, null=True),
            preserve_default=True,
        ),
    ]
