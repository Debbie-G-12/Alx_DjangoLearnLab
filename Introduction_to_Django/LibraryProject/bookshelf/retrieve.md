python manage.py shell
from bookshelf.models import Book
Book.objects.all()
Book.objects.get(id=1)
