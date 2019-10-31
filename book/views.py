from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, status, filters
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework.decorators import action
from rest_framework.response import Response
import django_filters
import requests
import json

from .models import Book, Author, IndustryIdentifies, ImageLinks
from .forms import BookForm, AuthorForm, ImageLinksForm, IndustryIdentifiesForm
from .filters import BookFilter
from . import serializers


class BookListView(ListView):
    model = Book
    template_name = "list.html"
    context_object_name = "books"

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
    success_url = "/identifier/add"
    template_name = "add.html"


class ImageCreateView(CreateView):
    model = ImageLinks
    form_class = ImageLinksForm
    success_url = "/image/add"
    template_name = "add.html"


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = "/identifier/add"
    template_name = "add.html"


def from_api(request):
    response = {}
    if 'query' in request.GET:
        query = request.GET['query']
        response = requests.get("https://www.googleapis.com/books/v1/volumes?q=%s" % query).json()['items']
    for books in response:
        try:
            element1 = books['volumeInfo']
            id_ = books['id']
            title = element1['title']
            language = element1['language']
            published_date = element1['publishedDate']
            book = Book(id=id_, title=title, language=language, published_date=published_date)
            book.save()
            try:
                small_th = element1['imageLinks']['smallThumbnail']
                th = element1['imageLinks']['thumbnail']
                imageLink = ImageLinks(small_thumbnail=small_th, thumbnail=th)
                imageLink.save()
                book.image_links = imageLink
                book.save()
            except:
                try:
                    small_th = element1['imageLinks']['smallThumbnail']
                    th = element1['imageLinks']['thumbnail']
                    imageLink = ImageLinks.objects.get(small_thumbnail=small_th, thumbnail=th)
                    book.image_links = imageLink
                    book.save()
                except:
                    pass

            try:
                page_count = element1['pageCount']
                book.page_count = page_count
                book.save()
            except:
                pass

            for author in element1['authors']:
                name = author
                try:
                    auth = Author(name=name)
                    auth.save()
                    book.authors.add(auth)
                except:
                    auth = Author.objects.get(name=name)
                    book.authors.add(auth)

            for identifier in element1['industryIdentifiers']:
                type_ = identifier['type']
                number = identifier['identifier']
                try:
                    idntf = IndustryIdentifies(type=type_, identifier=number)
                    idntf.save()
                    book.industry_identifies.add(idntf)
                except:
                    idntf = IndustryIdentifies.objects.get(type=type_, identifier=number)
                    book.industry_identifies.add(idntf)
        except:
            pass

    return render(request, 'fromapi.html', {'response': response})


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("title", "authors__name", "language", "published_date")


class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorsSerializer


class ImageLinksViewSet(viewsets.ModelViewSet):
    queryset = ImageLinks.objects.all()
    serializer_class = serializers.ImageSerializer


class IndustryIdentifyViewSet(viewsets.ModelViewSet):
    queryset = IndustryIdentifies.objects.all()
    serializer_class = serializers.IdentifiesSerializer
