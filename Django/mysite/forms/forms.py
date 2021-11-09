from os import name
from typing import Iterator
from django import forms
from .models import Author, Book
from django.utils import timezone



TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = ['name', 'title', 'birth_date']
    

# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = ['name', 'authors']

class AuthorForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    title = forms.ChoiceField(choices=TITLE_CHOICES)
    birth_date = forms.DateField()


class BookForm(forms.Form):
    name = forms.CharField(max_length=100)
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())