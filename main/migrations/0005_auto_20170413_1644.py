# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170413_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='body_type',
            field=models.CharField(choices=[('Sedan', 'Sedan'), ('Hatchback', 'Hatchback'), ('Wagon', 'Wagon')], default=('Hatchback', 'Hatchback'), max_length=255),
        ),
        migrations.AlterField(
            model_name='car',
            name='link',
            field=models.URLField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='car',
            name='phone_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone'),
        ),
    ]
