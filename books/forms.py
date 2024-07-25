from django.forms import ModelForm
from .models import Book


class BookCreationForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "price",
            "summary",
        ]
