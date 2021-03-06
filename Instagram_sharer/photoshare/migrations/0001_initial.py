# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-25 08:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstaPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('media_file', models.FileField(upload_to='')),
                ('tag', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sername', models.CharField(max_length=50)),
                ('access_token', models.CharField(max_length=100)),
                ('user_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoshare.InstaPost')),
            ],
        ),
    ]
