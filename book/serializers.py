from rest_framework import serializers

from book.models import Author, Book, IndustryIdentifies, ImageLinks


class AuthorsSerializer(serializers.ModelSerializer):
    """
    Serializing all the Authors
    """

    class Meta:
        model = Author
        fields = ["name"]


class ImageSerializer(serializers.ModelSerializer):
    """
    Serializing all the Image Links
    """

    class Meta:
        model = ImageLinks
        fields = ["small_thumbnail", "thumbnail"]


class IdentifiesSerializer(serializers.ModelSerializer):
    """
    Serializing all the Industry Identifies
    """

    class Meta:
        model = IndustryIdentifies
        extra = 2
        fields = ["type", "identifier"]


class BookSerializer(serializers.ModelSerializer):
    """
    Serializing all the Books
    """

    class Meta:
        model = Book
        fields = ["id", "title", "page_count", "language", "authors", "published_date", "industry_identifies", "image_links",]