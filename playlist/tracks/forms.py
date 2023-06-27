from django import forms
from .models import Author, Music


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['name', 'surname', 'age']


class MusicForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Music
        fields = ['title', 'description', 'author', 'genre', 'release_date', 'personal_thoughts']

