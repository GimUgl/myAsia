# Generated by Django 4.2 on 2024-03-31 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myAsia_blog', '0008_alter_books_created_at_alter_comment_comment_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ['created_at'], 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
    ]
