import django_filters
from rest_framework import viewsets, filters

from .models import User, Book
from .serializer import UserSerializer, BookSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  filter_fields = ('title', 'publisher', 'author', 'status')
