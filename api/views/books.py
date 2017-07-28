from rest_framework import generics

from api.models import Book
from api.serializers import BookSerializer


class BookList(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating Book objects
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
