# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=128)),
                ('lastName', models.CharField(max_length=128)),
                ('age', models.IntegerField()),
                ('picture', models.ImageField(upload_to=b'profile_pictures')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Oefeningenreeks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Opgave',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('picture', models.ImageField(upload_to=b'Opgaves')),
                ('optie1', models.CharField(default=b'', max_length=128)),
                ('optie2', models.CharField(default=b'', max_length=128, null=True)),
                ('optie3', models.CharField(default=b'', max_length=128, null=True)),
                ('optie4', models.CharField(default=b'', max_length=128, null=True)),
                ('correctAnswer', models.IntegerField(default=1)),
                ('category', models.CharField(max_length=2, choices=[(b'1', b'Bijwoord'), (b'2', b'Lidwoord')])),
                ('difficulty', models.CharField(default=b'1', max_length=2, choices=[(b'0', b'Easy'), (b'1', b'Medium'), (b'2', b'Hard')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resultaat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('grade', models.IntegerField(default=0)),
                ('child', models.ForeignKey(to='oefening.Child')),
                ('oefeningenreeks', models.ForeignKey(to='oefening.Oefeningenreeks')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='oefeningenreeks',
            name='oefeningen',
            field=models.ManyToManyField(to='oefening.Opgave'),
            preserve_default=True,
        ),
    ]
