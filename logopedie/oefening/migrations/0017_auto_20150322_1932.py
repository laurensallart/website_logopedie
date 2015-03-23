# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oefening', '0016_auto_20150318_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.IntegerField(default=1)),
                ('correctAnswer', models.IntegerField()),
                ('child', models.ForeignKey(to='oefening.Child')),
                ('opgave', models.ForeignKey(to='oefening.Opgave')),
                ('resultaat', models.ForeignKey(to='oefening.Resultaat')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='resultaat',
            name='wrong',
        ),
        migrations.AlterField(
            model_name='resultaat',
            name='total',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
