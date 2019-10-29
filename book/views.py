from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, status, filters
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework.decorators import action
from rest_framework.response import Response
import datetime

from .models import Book, Author, IndustryIdentifies, ImageLinks
from .forms import BookForm, AuthorForm, ImageLinksForm, IndustryIdentifiesForm
from .filters import BookFilter


class BookListView(ListView):
    model = Book
    template_name = "list.html"
    context_object_name = "books"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = BookFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostCreateView(CreateView):
    model = Book
    form_class = BookForm
    success_url = "/book/add"
    template_name = "add.html"


class IndustryCreateView(CreateView):
    model = IndustryIdentifies
    form_class = IndustryIdentifiesForm
    success_url = "/image/add"
    template_name = "add.html"


class ImageCreateView(CreateView):
    model = ImageLinks
    form_class = ImageLinksForm
    success_url = "/book/add"
    template_name = "add.html"


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = "/identifier/add"
    template_name = "add.html"