# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-28 11:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photoshare', '0002_instapost_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='sername',
            new_name='user_id',
        ),
    ]