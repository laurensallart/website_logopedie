# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oefening', '0019_resultaat_ended'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resultaat',
            old_name='answer',
            new_name='answers',
        ),
    ]
