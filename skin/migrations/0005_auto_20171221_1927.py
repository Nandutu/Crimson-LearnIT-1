# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-21 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skin', '0004_auto_20171221_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactpage',
            name='suggestion',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='skintype',
            name='image',
            field=models.ImageField(default=b'vol5-4.png', upload_to=b''),
        ),
    ]