from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name = 'welcome'),
    path('home/', views.home, name = 'home'),
    path('all_books/', views.all_books, name = 'all_books'),
    path('genre/<str:slug>', views.category_detail, name = 'category_detail'),
    path('pdf/<str:slug>', views.book_detail, name = 'book_detail'),
    path('searched_books/', views.search_book, name = 'book_search'),
    path('Video/', views.Videos, name = 'video'),
    path('Download/', views.download, name = 'download'),    
]