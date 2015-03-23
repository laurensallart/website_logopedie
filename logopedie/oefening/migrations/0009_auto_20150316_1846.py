# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oefening', '0008_auto_20150316_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oefeningenreeks',
            name='oefeningen',
            field=models.ManyToManyField(to='oefening.Opgave', null=True, blank=True),
            preserve_default=True,
        ),
    ]
