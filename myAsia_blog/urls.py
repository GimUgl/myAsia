from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('genres/<int:genres_id>/', views.get_genres_books_view, name='genres_books'),
    path('login/', views.login_view, name='login'),
    path('registration/', views.registration_view, name='registration'),
    path('logout/', views.user_logout, name='logout'),
    path('detail/<int:book_pk>/', views.book_detail, name='detail'),
    path('create/', views.create_book, name='create'),
    path('update/<int:pk>/', views.UpdateBook.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteBook.as_view(), name='delete'),
    path('search/', views.SearchResults.as_view(), name='search'),
    path('user_page/<int:user_pk>/', views.user_page_view, name='user_page'),
    path('read/<int:book_pk>/', views.fb2_reader_view, name='reader'),
    # path('<str:obj_type>/<int:obj_id>/<str:action>/', views.add_vote, name='add_vote'),
]