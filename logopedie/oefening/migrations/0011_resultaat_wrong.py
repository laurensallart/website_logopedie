# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oefening', '0010_auto_20150316_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultaat',
            name='wrong',
            field=models.ManyToManyField(to='oefening.Opgave', null=True, blank=True),
            preserve_default=True,
        ),
    ]
