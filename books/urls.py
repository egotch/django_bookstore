from django.urls import path

from .views import BookListView, BookDetailView, BookCreateView

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("addbook/", BookCreateView.as_view(), name="book_add"),
    path("<uuid:pk>/", BookDetailView.as_view(), name="book_detail"),
]
