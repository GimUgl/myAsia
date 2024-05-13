from django.shortcuts import render, redirect
from .models import Books, Genres, Comment, BookCountViews, Like, Dislike
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistationForm, CommentForm, BooksForm
from django.views.generic import UpdateView, DeleteView, ListView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.models import User

from bs4 import BeautifulSoup
import os
from myAsia.settings import BASE_DIR
import xml.etree.ElementTree as ET
from lxml import etree

# Онлайн читалка
def fb2_reader_view(request, book_pk):
    book = Books.objects.get(pk=book_pk)

    dir_url = os.path.join(BASE_DIR)
    dir_url1 = dir_url.split('\\')
    r_url1 = dir_url1[0] + '/' + dir_url1[1] + '/' + dir_url1[2] + '/'

    file_url = os.path.join(book.files.url)
    file_url1 = file_url.split('/')
    r_url2 = file_url1[1] + '/' + file_url1[2] + '/' + file_url1[3] + '/' + file_url1[4]

    r_url = r_url1 + r_url2

    # with open(r_url, encoding="utf-8") as file:
    #     src = file.read()
    #
    # soup = BeautifulSoup(src, 'xml')
    #
    # find_body_section = soup.find('body').find_all('section')
    # print(find_body_section)

    fb2_file = r_url
    txt_file = 'D:/django_project/myAsia/media/files/books/txt_file.txt'
    tree = ET.parse(fb2_file)
    root = tree.getroot()

    text = ""
    for body in root.iter("{http://www.gribuser.ru/xml/fictionbook/2.0}body"):
        for p in body.iter("{http://www.gribuser.ru/xml/fictionbook/2.0}p"):
            text += str(p.text) + "\n"
    with open(txt_file, "w", encoding='utf-8') as file:
        file.write(text)


    with open(txt_file, 'r', encoding='utf-8') as f:
        content = f.read()


    # for line in lines:
    #     content = line.replace('\n', ''))


    # for poisk_vsex_p in find_body_section:
    #     find_all_p = poisk_vsex_p.find('p').text
    #     print(find_all_p)

    context = {
        # 'find_body_section': find_body_section,
        # 'text': text,
        'content': content,
    }
    return render(request, 'myAsia_blog/fb2_reader.html', context)


# Авторизация
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()

    context = {
        'form': form
    }
    return render(request, 'myAsia_blog/login.html', context)


# Регистрация
def registration_view(request):
    if request.method == 'POST':
        form = RegistationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistationForm()

    context = {
        'form': form
    }
    return render(request, 'myAsia_blog/registration.html', context)


# Выход с аккаунта
def user_logout(request):
    logout(request)
    return redirect('home')


# Навбар
def get_genres_books_view(request, genres_id):
    genres = Genres.objects.get(pk=genres_id)
    books = Books.objects.filter(genres=genres)

    context = {
        'genres': genres,
        'books': books
    }
    return render(request, 'myAsia_blog/index.html', context)


# Детальная страница
def book_detail(request, book_pk):
    book = Books.objects.get(pk=book_pk)
    comments = Comment.objects.filter(book=book)

    # try:
    #     book.likes
    # except Exception as e:
    #     Like.objects.create(book=book)
    #
    # try:
    #     book.dislikes
    # except Exception as e:
    #     Dislike.objects.create(book=book)

    paginator = Paginator(comments, 10)
    page = request.GET.get('page')
    comments = paginator.get_page(page)

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.book = book
            form.author = request.user
            form.save()

            return redirect('detail', book.pk)
    else:
        form = CommentForm()

    if not request.session.session_key:
        request.session.save()

    session_id = request.session.session_key

    viewed_books = BookCountViews.objects.filter(book=book, session_id=session_id)

    if viewed_books.count() == 0 and session_id != 'None':
        viewed = BookCountViews()
        viewed.book = book
        viewed.session_id = session_id
        viewed.save()
        book.views += 1
        book.save()

    context = {
        'book': book,
        'form': form,
        'comments': comments,
    }
    return render(request, 'myAsia_blog/detail.html', context)


# Добавление книги
@login_required(login_url='login')
def create_book(request):
    if request.method == 'POST':
        form = BooksForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('detail', form.pk)
    else:
        form = BooksForm()

    context = {
        'form': form,
    }

    return render(request, 'myAsia_blog/book_form.html', context)


# Главная страница
class HomePageView(ListView):
    model = Books
    template_name = 'myAsia_blog/index.html'
    context_object_name = 'books'


# Поисковая строка
class SearchResults(HomePageView):
    def get_queryset(self):
        query = self.request.GET.get('book')
        return Books.objects.filter(
            Q(book__iregex=query) | Q(isbn__regex=query) | Q(short_description__iregex=query)
        )


# Обновление книги
class UpdateBook(UpdateView):
    model = Books
    form_class = BooksForm
    template_name = 'myAsia_blog/book_form.html'


# Удаление книги
class DeleteBook(DeleteView):
    model = Books
    template_name = 'myAsia_blog/book_confirm_delete.html'
    success_url = '/'
    context_object_name = 'books'


# Страница пользователя
def user_page_view(request, user_pk):
    user = User.objects.get(pk=user_pk)
    book = Books.objects.filter(author=user)
    book_count = len(book)

    context = {
        'user': user,
        'book': book,
        'book_count': book_count,
    }
    return render(request, 'myAsia_blog/user_page.html', context)
