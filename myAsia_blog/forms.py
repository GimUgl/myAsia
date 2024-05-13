from django.contrib.auth.models import User

from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Comment, Books

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['book', 'isbn', 'short_description', 'description', 'image', 'files', 'genres']
        widgets = {
            'book': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название книги. Не более 150 символов'
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите isbn'
            }),
            'short_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите краткое описание. Не более 300 символов',
                'rows': 4
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите полное описание',
                'rows': 10
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'files': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Загрузить книгу'
            }),
            'genres': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Выберите жанр книги'
            })
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш комментарий',
                'rows': 2
            })
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя пользователя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль'
    }))

    class Meta:
        model = User

class RegistationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Подтвердите пароль'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя пользователя'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите почту'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Ваше имя'
            })
        }