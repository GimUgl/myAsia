# Generated by Django 4.2 on 2024-04-14 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myAsia_blog', '0014_alter_comment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='files/books/', verbose_name='Файл книги'),
        ),
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photo/books/', verbose_name='Обложка книги'),
        ),
        migrations.CreateModel(
            name='BookCountViews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=300)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myAsia_blog.books')),
            ],
        ),
    ]
