# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoshare', '0005_instapost_user_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
                ('taged_post', models.ManyToManyField(to='photoshare.InstaPost')),
            ],
        ),
    ]
