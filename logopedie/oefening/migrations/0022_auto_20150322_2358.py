# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oefening', '0021_auto_20150322_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='correctAnswer',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
