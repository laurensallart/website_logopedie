# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oefening', '0002_opgave_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opgave',
            name='test',
        ),
        migrations.AddField(
            model_name='resultaat',
            name='total',
            field=models.IntegerField(default=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='child',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'profile_pictures'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='opgave',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'Opgaves'),
            preserve_default=True,
        ),
    ]
