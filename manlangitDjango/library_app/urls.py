from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='library_index'),
    path('available-books/', views.available_books, name='available_books'),
    path('borrow-book/', views.borrow_book, name='borrow_book'),
]
