# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oefening', '0018_auto_20150322_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultaat',
            name='ended',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
