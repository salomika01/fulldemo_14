from django.urls import path
from .views import (MusicListView, MusicDetailView, MusicCreateView,
                    MusicUpdateView, MusicDeleteView, AuthorListView,
                    AuthorDetailView, AuthorCreateView, AuthorUpdateView,
                    AuthorDeleteView)

urlpatterns = [
    path('', MusicListView.as_view(), name='music_list'),
    path('music/<int:pk>/', MusicDetailView.as_view(), name='music_detail'),
    path('music/new/', MusicCreateView.as_view(), name='music_new'),
    path('music/<int:pk>/edit/', MusicUpdateView.as_view(), name='music_edit'),
    path('music/<int:pk>/delete/', MusicDeleteView.as_view(), name='music_delete'),

    path('author/', AuthorListView.as_view(), name='author_list'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('author/new/', AuthorCreateView.as_view(), name='author_new'),
    path('author/<int:pk>/edit/', AuthorUpdateView.as_view(), name='author_edit'),
    path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),
    ]




