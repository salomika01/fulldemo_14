from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Music, Author
from .forms import MusicForm, AuthorForm


class MusicListView(ListView):
    model = Music
    template_name = 'musics/music_list.html'
    context_object_name = 'musics'


class MusicDetailView(DetailView):
    model = Music
    template_name = 'musics/music_detail.html'


class MusicCreateView(CreateView):
    model = Music
    form_class = MusicForm
    template_name = 'musics/music_edit.html'
    success_url = reverse_lazy('music_list')


class MusicUpdateView(UpdateView):
    model = Music
    form_class = MusicForm
    template_name = 'musics/music_edit.html'
    success_url = reverse_lazy('music_list')


class MusicDeleteView(DeleteView):
    model = Music
    template_name = 'musics/music_confirm_delete.html'
    success_url = reverse_lazy('music_list')


class AuthorListView(ListView):
    model = Author
    template_name = 'authors/author_list.html'
    context_object_name = 'authors'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authors/author_detail.html'


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'authors/author_edit.html'
    success_url = reverse_lazy('author_list')


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'authors/author_edit.html'
    success_url = reverse_lazy('author_list')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'authors/author_confirm_delete.html'
    success_url = reverse_lazy('author_list')