from forms.models import Author, Book
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .forms import BookForm, AuthorForm
from django.views import generic
from django.urls import reverse


class Index(generic.ListView):
    model = Book
    template_name = 'forms/index.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data




class AuthorUpdateView(generic.UpdateView):
    model = Author
    form_class = AuthorForm
    # fields = '__all__'
    template_name = 'forms/author_update_form.html'
    # template_name_suffix = '_update_form'
    success_url = '/forms/authors'

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault('content_type', self.content_type)

        a = self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs
        )
        return a
        # return super().render_to_response(context, **response_kwargs)

    def post(self, request, *args, **kwargs):
        print('hello')
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('hello2')
        return super().form_valid(form)


def AuthorUpdate(request, pk):
    instance = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(instance=instance, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('form:authors'))

    else:
        form = AuthorForm(instance=instance)
    return render(request, 'forms/author_update_form.html', {'form': form})


def get_book(request):
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            # new_book = Book.objects.create(name=name)
            # new_book.authors.set(authors)

            return HttpResponseRedirect(reverse('form:books'))

    else:
        form = BookForm()
        # print(form.as_table())
    return render(request, 'forms/books.html', {'form': form})



def get_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            # new_author = form.cleaned_data
            # Author.objects.create(**new_author)
            # return HttpResponseRedirect(reverse('form:authors'))
            return redirect('form:author_details', pk=author.id)

    else:
        form = AuthorForm()
    return render(request, 'forms/add_author.html', {'form': form})




# ----------------------------- CRUD AUTHOR ----------------------------------


class AuthorView(generic.ListView):
    model = Author
    template_name = 'forms/authors.html'
    context_object_name = 'form'


class AuthorDetails(generic.DetailView):
    model = Author
    template_name = 'forms/author_details.html'
    context_object_name = 'form'


class DelAuthor(generic.DeleteView):
    model = Author
    success_url = '/forms/authors'


class UpdateAuthor(generic.UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'forms/author_update_form.html'

    def get_success_url(self):
        return reverse('form:author_details', args=[self.kwargs['pk']])


class AddAuthor(generic.CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'forms/add_author.html'

    def get_success_url(self):
        author = self.object
        return reverse('form:author_details', args=[author.pk])
