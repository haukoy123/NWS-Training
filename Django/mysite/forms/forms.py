from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import DateInput
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
    name = forms.CharField(label='Name', max_length=100, widget=forms.Textarea())
    title = forms.ChoiceField(choices=TITLE_CHOICES)
    birth_date = forms.DateField(widget=DateInput({'type':'date'}))

    def clean(self):
        clean_data = super().clean()
        if clean_data['name'] == 'hau' and clean_data['title'] == 'MR':
            raise ValidationError('khong duoc chon MR')
        clean_data['title'] = 'MS'
        return clean_data

    def clean_birth_date(self):
        if self.cleaned_data['birth_date'] > timezone.now().date():
            raise ValidationError('ngay sinh nho hon hien tai')
        return self.cleaned_data['birth_date']


class BookForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'class':'book', 'style':'background:#e4dfdf;'}
        )
    )
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            {'class':'author'}
        )
    )

    # name.widget.attrs.update(attrs={'class':'book', 'style':'background:#e4dfdf;'})
