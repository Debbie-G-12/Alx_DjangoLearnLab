python manage.py shell
from bookshelf.models import Book
Book.objects.create(title='1984', author='George Orwell', publication_year=1949, isbn='1234567890123')
