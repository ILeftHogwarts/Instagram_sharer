# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoshare', '0008_auto_20170830_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instapost',
            name='url',
            field=models.CharField(default='default', max_length=100),
        ),
    ]