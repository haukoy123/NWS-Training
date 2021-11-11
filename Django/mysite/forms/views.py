from forms.models import Author, Book
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import BookForm, AuthorForm
from django.views import generic

class Index(generic.ListView):
    model = Book
    template_name = 'forms/index.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # print(a['object_list'][0].name)
        # print(a['object_list'][0].authors.name)
        return context_data


def get_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            authors = form.cleaned_data['authors']
            new_book = Book.objects.create(name=name)
            new_book.authors.set(authors)
            # print(form.data)
            # # print('hello')
            # print(form.cleaned_data['name'])
            return HttpResponseRedirect(reverse('form:books'))

    else:
        form = BookForm()
        # print(form.as_table())
    return render(request, 'forms/books.html', {'form': form})



def get_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = form.cleaned_data
            Author.objects.create(**new_author)
            return HttpResponseRedirect(reverse('form:authors'))
    else:
        form = AuthorForm()
    return render(request, 'forms/authors.html', {'form': form})
