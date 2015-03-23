# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oefening', '0005_auto_20150314_1103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opgave',
            old_name='slugger',
            new_name='slug',
        ),
    ]
