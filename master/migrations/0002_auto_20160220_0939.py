# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 07:39
from __future__ import unicode_literals

import ckeditor.fields
import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import master.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('article_title', models.CharField(blank=True, max_length=200, unique=True, verbose_name='Заголовок статьи')),
                ('metakey', models.CharField(blank=True, max_length=255, verbose_name='Ключевые слова')),
                ('metadesc', models.CharField(blank=True, max_length=255, verbose_name='Мета описание')),
                ('image', models.ImageField(blank=True, default='no_image_povaryonok.png', upload_to=master.models.make_upload_path, verbose_name='Изображение')),
                ('article_anons', ckeditor.fields.RichTextField(blank=True, verbose_name='Анонс статьи')),
                ('article_text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Полный текст статьи')),
                ('article_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('recipe', models.BooleanField(default=None, verbose_name='Рецепт')),
                ('article_publish', models.BooleanField(default=True, verbose_name='Опубликован')),
            ],
            options={
                'verbose_name_plural': 'Статьи и рецепты',
                'db_table': 'articles',
                'verbose_name': 'Статья, рецепт',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('category_name', models.CharField(db_index=True, default='', max_length=200, unique=True, verbose_name='Категория')),
                ('in_header', models.SmallIntegerField(blank=True, default=0, null=True, verbose_name='Категория в шапке сайта')),
                ('class_in_header', models.CharField(blank=True, default=False, max_length=20, null=True)),
            ],
            options={
                'verbose_name_plural': 'категории',
                'db_table': 'categories',
                'verbose_name': 'категория',
                'ordering': ['category_id'],
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('user_name', models.CharField(max_length=50, verbose_name='Имя пользователя')),
                ('comment_date', models.DateField(default=datetime.datetime.now, verbose_name='Дата')),
                ('comments_text', models.TextField(blank=True, verbose_name='Кометарий')),
                ('comments_article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='com', to='master.Articles', verbose_name='Коментарий для статьи')),
            ],
            options={
                'verbose_name_plural': 'коментарии',
                'db_table': 'comments',
                'verbose_name': 'коментарий',
                'ordering': ['-comment_date'],
            },
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('page_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=200, unique=True, verbose_name='Страница')),
                ('metakey', models.CharField(blank=True, max_length=255, verbose_name='Ключевые слова')),
                ('metadesc', models.CharField(blank=True, max_length=255, verbose_name='Мета описание')),
                ('slug', models.CharField(blank=True, max_length=250, verbose_name='Урл')),
                ('page_text', ckeditor.fields.RichTextField(blank=True, verbose_name='Текст страницы')),
                ('position', models.SmallIntegerField(verbose_name='Позиция')),
            ],
            options={
                'verbose_name_plural': 'страницы',
                'db_table': 'pages',
                'verbose_name': 'страница',
                'ordering': ['position'],
            },
        ),
        migrations.AddField(
            model_name='articles',
            name='category_article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.Categories', verbose_name='Категория статьи'),
        ),
    ]
