# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0002_laptop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dateout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateoutbutton', models.CharField(max_length=2)),
                ('dateout', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
