# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='announced_price',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='body_type',
            field=models.CharField(choices=[('Hatchback', 'Hatchback'), ('Sedan', 'Sedan'), ('Wagon', 'Wagon')], default=('Sedan', 'Sedan'), max_length=255),
        ),
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='number_of_owners',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='phone_number',
            field=models.CharField(max_length=255, null=True, verbose_name='79200393289'),
        ),
    ]