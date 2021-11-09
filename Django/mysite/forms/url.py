from django.urls import path
from . import views

app_name = 'form'

urlpatterns = [
    path('books/', views.get_book, name='books'),
]