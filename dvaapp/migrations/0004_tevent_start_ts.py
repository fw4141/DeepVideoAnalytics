# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0003_auto_20170802_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='tevent',
            name='start_ts',
            field=models.DateTimeField(null=True, verbose_name='date started'),
        ),
    ]
