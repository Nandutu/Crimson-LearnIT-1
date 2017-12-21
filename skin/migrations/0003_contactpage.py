# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-21 10:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('skin', '0002_skintype_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggestion', models.TextField(max_length=4000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('phone', models.IntegerField(max_length=15)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cpages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
