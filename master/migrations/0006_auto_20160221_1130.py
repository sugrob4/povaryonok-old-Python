# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0005_auto_20160221_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='article_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата'),
        ),
    ]
