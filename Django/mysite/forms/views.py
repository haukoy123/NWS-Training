from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import BookForm, AuthorForm


# def index(request):
    


def get_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            print(form.data)
            # print('hello')
            return HttpResponseRedirect(reverse('form:books'))

    else:
        form = BookForm()
        # print(form.as_table())
    return render(request, 'forms/books.html', {'form': form})