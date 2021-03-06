# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 18:51
from __future__ import unicode_literals

from django.db import migrations, models
import manager_files.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field='height', upload_to=manager_files.utils.UploadPath('uploads'), verbose_name='Image', width_field='width')),
                ('height', models.PositiveIntegerField(blank=True, default='100', editable=False, null=True)),
                ('width', models.PositiveIntegerField(blank=True, default='100', editable=False, null=True)),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='Date added')),
            ],
        ),
    ]
