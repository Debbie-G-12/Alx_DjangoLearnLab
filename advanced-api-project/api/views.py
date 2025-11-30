from rest_framework import generics, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

# ----------------------------
# Book Views for DRF API
# ----------------------------

# List view with filtering, searching, and ordering
class BookListView(generics.ListAPIView):
    """
    API endpoint that allows users to view all books.
    Supports:
    - Filtering by title, author name, and publication year
    - Searching by title and author name
    - Ordering by title and publication year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']  # filtering
    search_fields = ['title', 'author__name']  # search
    ordering_fields = ['title', 'publication_year']  # ordering
    ordering = ['title']  # default ordering

# Retrieve a single book
class BookDetailView(generics.RetrieveAPIView):
    """
    API endpoint to retrieve a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # accessible by anyone

# Create a new book (authenticated users only)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Update an existing book (authenticated users only)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Delete a book (authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
