# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_car_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='announced_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(blank=True, choices=[('White', 'White'), ('Red', 'Red'), ('Dark grey', 'Dark grey'), ('Blue', 'Blue'), ('Silver', 'Silver'), ('Silver-blue', 'Silver-blue'), ('Silver-beige', 'Silver-beige'), ('Black', 'Black')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='negotiated_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='number_of_owners',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='phone_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='79200393289'),
        ),
    ]
