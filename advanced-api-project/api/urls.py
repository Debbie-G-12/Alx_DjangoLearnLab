from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),            # list with filter/search/order
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'), # retrieve single book
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # create book
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'), # update
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'), # delete
]
