# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0003_bank_ul'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='bank_ul',
            name='description',
            field=models.TextField(default=''),
        ),
    ]