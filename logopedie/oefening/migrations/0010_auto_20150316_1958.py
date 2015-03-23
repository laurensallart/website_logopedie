# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oefening', '0009_auto_20150316_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultaat',
            name='oefeningenreeks',
            field=models.ForeignKey(default=None, to='oefening.Oefeningenreeks'),
            preserve_default=True,
        ),
    ]
