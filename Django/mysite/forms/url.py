from django.urls import path
from . import views

app_name = 'form'

urlpatterns = [
    path('books/', views.get_book, name='books'),
    # path('authors/', views.get_author, name='authors'),
    path('index/', views.Index.as_view(), name='index'),
    # path('authors/<int:pk>/', views.AuthorUpdateView.as_view(), name='author_update'),


    path('authors/', views.AuthorView.as_view(), name='authors'),
    path('authors/<int:pk>/update/', views.UpdateAuthor.as_view(), name='update_author'),
    path('authors/<int:pk>/delete/', views.DelAuthor.as_view(), name='del_author'),
    path('authors/<int:pk>/', views.AuthorDetails.as_view(), name='author_details'),
    path('authors/add_author/', views.AddAuthor.as_view(), name='add_author'),
]
