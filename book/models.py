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
    authors = models.ManyToManyField(Author)
    published_date = PartialDateField()
    industry_identifies = models.ManyToManyField(IndustryIdentifies)
    page_count = models.IntegerField(null=False)
    image_links = models.OneToOneField(ImageLinks, on_delete=models.CASCADE)
    language = models.CharField(max_length=3, null=False)

    def __str__(self):
        return self.title