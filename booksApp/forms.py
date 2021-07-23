from django import forms
from .models import book


class add_book_form(forms.ModelForm):
    class Meta:
        model = book
        fields ='__all__'
        exclude=('publisher','craeted_date','slug')