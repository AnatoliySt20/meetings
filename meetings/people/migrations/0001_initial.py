# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-11 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('school', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('photography', models.ImageField(upload_to='personal_images/')),
            ],
        ),
    ]
