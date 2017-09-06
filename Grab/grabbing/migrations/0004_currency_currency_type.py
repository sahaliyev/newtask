# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grabbing', '0003_remove_currency_currency_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='currency_type',
            field=models.IntegerField(choices=[(1, 'cash'), (2, 'nocash')], default=1),
        ),
    ]