from django.db import models
from partial_date import PartialDateField

class Author(models.Model):
    name = models.CharField(max_length=128, null=False, unique=True)

    def __str__(self):
        return self.name


class ImageLinks(models.Model):
    small_thumbnail = models.URLField()
    thumbnail = models.URLField()


class IndustryIdentifies(models.Model):
    type = models.CharField(max_length=10)
    identifier = models.CharField(max_length=20, primary_key=True)


class Book(models.Model):
    id = models.CharField(max_length=16, primary_key=True, unique=True, null=False)
    title = models.CharField(max_length=128, null=False)
    authors = models.ManyToManyField(Author, blank=True)
    published_date = PartialDateField(blank=True)
    industry_identifies = models.ManyToManyField(IndustryIdentifies, blank=True)
    page_count = models.IntegerField(null=True)
    image_links = models.OneToOneField(ImageLinks, on_delete=models.CASCADE, blank=True)
    language = models.CharField(max_length=3, null=True)

    def __str__(self):
        return self.title