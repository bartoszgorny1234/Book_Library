"""book_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based viewsTrochę
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book.views import BookListView, PostCreateView, IndustryCreateView, ImageCreateView, AuthorCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("book/add/", PostCreateView.as_view(), name="book_add"),
    path("author/add/", AuthorCreateView.as_view(), name="author_add"),
    path("image/add/", ImageCreateView.as_view(), name="image_add"),
    path("identifier/add/", IndustryCreateView.as_view(), name="identifier_add"),
    path('books/', BookListView.as_view(), name='book_list')

]
