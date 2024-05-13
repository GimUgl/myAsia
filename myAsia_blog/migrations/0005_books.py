# Generated by Django 5.0.1 on 2024-02-03 14:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAsia_blog', '0004_rename_genre_genres'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(max_length=150, unique=True, verbose_name='Название книги')),
                ('isbn', models.CharField(max_length=20, unique=True, verbose_name='ISBN книги')),
                ('short_description', models.CharField(max_length=300, verbose_name='Краткое описание книги')),
                ('description', models.TextField(verbose_name='Описание книги')),
                ('files', models.FileField(blank=True, null=True, upload_to='files/books/', verbose_name='Файл')),
                ('views', models.IntegerField(default=0, verbose_name='Кол-во просмотров')),
                ('download', models.IntegerField(default=0, verbose_name='Кол-во скачиваний')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('genres', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='myAsia_blog.genres', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['book'],
            },
        ),
    ]
