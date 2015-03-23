# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oefening', '0017_auto_20150322_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='resultaat',
        ),
        migrations.AddField(
            model_name='resultaat',
            name='answer',
            field=models.ManyToManyField(to='oefening.Answer', null=True, blank=True),
            preserve_default=True,
        ),
    ]
