# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-10-19 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_auto_20191012_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='labdetail',
            name='logo',
            field=models.ImageField(default='default/default.png', upload_to='LabLogo/%Y/%m/%d'),
        ),
    ]
