from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


class BookListCreateView(generics.ListCreateAPIView):
    """
    Handles:
    - GET: List all books (public)
    - POST: Create a new book (authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles:
    - GET: Retrieve a book (public)
    - PUT/PATCH: Update a book (authenticated)
    - DELETE: Delete a book (authenticated)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
