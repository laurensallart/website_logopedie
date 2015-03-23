# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oefening', '0022_auto_20150322_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opgave',
            name='category',
            field=models.CharField(max_length=2, choices=[(b'1', b'Woordenschat'), (b'2', b'Bijwoorden'), (b'2', b'Ander')]),
            preserve_default=True,
        ),
    ]
