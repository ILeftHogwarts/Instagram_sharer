# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoshare', '0009_auto_20170830_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='instapost',
            name='type',
            field=models.CharField(choices=[('videos', 'video'), ('images', 'image')], default='image', max_length=6),
        ),
    ]
