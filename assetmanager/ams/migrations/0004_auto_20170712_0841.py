# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0003_dateout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datein',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateinbutton', models.CharField(max_length=1)),
                ('datein', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='dateout',
            name='dateoutbutton',
            field=models.CharField(max_length=1),
        ),
    ]
