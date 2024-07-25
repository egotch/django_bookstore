from django.views.generic import ListView, DetailView
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.base import HttpResponseRedirect
from django.shortcuts import render
from .forms import BookCreationForm
from .models import Book


# TODO: Create a way for users to add their own book (not through the admin)
class BookListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/book_list.html"


class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"


class BookCreateView(View):
    form_class = BookCreationForm
    success_url = reverse_lazy("book_list")
    template_name = "books/book_create.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_book = form.save(commit=False)
            new_book.save()
            return HttpResponseRedirect(reverse_lazy("book_list"))
