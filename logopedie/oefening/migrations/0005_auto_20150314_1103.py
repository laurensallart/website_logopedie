# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oefening', '0004_auto_20150314_1101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opgave',
            old_name='slug',
            new_name='slugger',
        ),
    ]
