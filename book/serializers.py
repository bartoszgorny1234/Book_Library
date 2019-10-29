from rest_framework import serializers

from book.models import Author, Book, IndustryIdentifies, ImageLinks


class AuthorsSerializer(serializers.ModelSerializer):
    """
    Serializing all the Authors
    """

    class Meta:
        model = Author
        fields = ("name")


class ImageSerializer(serializers.ModelSerializer):
    """
    Serializing all the Image Links
    """

    class Meta:
        model = ImageLinks
        fields = ("smallThumbnail", "thumbnail")


class IdentifiesSerializer(serializers.ModelSerializer):
    """
    Serializing all the Industry Identifies
    """

    class Meta:
        model = IndustryIdentifies
        fields = ("type", "identifier")


class BookSerializer(serializers.ModelSerializer):
    """
    Serializing all the Books
    """
    authors = AuthorsSerializer(many=True)
    image_links = ImageSerializer()
    industry_identifies = IndustryIdentifies(many=True)

    class Meta:
        model = Book
        fields = ("id", "title", "authors", "publishedDate", "industryIdentifies", "page_count", "imageLinks", "language")
