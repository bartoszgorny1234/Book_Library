from django import forms
from book.models import Author, IndustryIdentifies, ImageLinks, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ("__all__")


class IndustryIdentifiesForm(forms.ModelForm):
    class Meta:
        model = IndustryIdentifies
        fields = ("__all__")


class ImageLinksForm(forms.ModelForm):
    class Meta:
        model = ImageLinks
        fields = ("__all__")


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("__all__")

    # id = models.CharField(max_length=16, primary_key=True, unique=True, null=False)
    # # title = models.CharField(max_length=128, null=False)
    # authors = models.ManyToManyField(Author)
    # # published_date = PartialDateField()
    # industry_identifies = models.ManyToManyField(IndustryIdentifies)
    # page_count = models.IntegerField(null=False)
    # image_links = models.OneToOneField(ImageLinks, on_delete=models.CASCADE)
    # language = models.CharField(max_length=3, null=False)