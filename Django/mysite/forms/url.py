from django.urls import path
from . import views

app_name = 'form'

urlpatterns = [
    path('books/', views.get_book, name='books'),
    path('authors/', views.get_author, name='authors'),
    path('index/', views.Index.as_view(), name='index'),
]
