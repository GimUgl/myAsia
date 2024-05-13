from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class Genres(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Жанр')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Books(models.Model):
    book = models.CharField(max_length=150, unique=True, verbose_name='Название книги')
    isbn = models.CharField(max_length=20, unique=True, verbose_name='ISBN книги', blank=True, null=True)
    short_description = models.CharField(max_length=300, verbose_name='Краткое описание книги')
    description = models.TextField(verbose_name='Описание книги')
    image = models.ImageField(verbose_name='Обложка книги', upload_to='photo/books/', blank=True, null=True)
    files = models.FileField(verbose_name='Файл книги', upload_to='files/books/', blank=True, null=True)
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    download = models.IntegerField(default=0, verbose_name='Кол-во скачиваний')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='books')
    recommended_books = models.BooleanField(default=False, blank=True, null=True)

    genres = models.ForeignKey(Genres, on_delete=models.CASCADE, verbose_name='Жанр', related_name='books')

    def __str__(self):
        return f'{self.book}'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_pk': self.pk})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-created_at']


class BookCountViews(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=300)


class Like(models.Model):
    user = models.ManyToManyField(User, related_name='likes')
    book = models.OneToOneField(Books, on_delete=models.CASCADE, related_name='likes', blank=True, null=True)

class Dislike(models.Model):
    user = models.ManyToManyField(User, related_name='dislikes')
    book = models.OneToOneField(Books, on_delete=models.CASCADE, related_name='dislikes', blank=True, null=True)


class Comment(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name='Книга', related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='comments')
    comment = models.TextField(max_length=1000, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.book} : {self.author}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']
