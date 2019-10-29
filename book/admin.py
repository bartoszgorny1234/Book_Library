from django.contrib import admin
from book.models import Author, Book, IndustryIdentifies, ImageLinks

admin.site.register(Author)
admin.site.register(IndustryIdentifies)
admin.site.register(ImageLinks)
admin.site.register(Book)

# Register your models here.
