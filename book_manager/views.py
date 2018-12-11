import django_filters
from rest_framework import viewsets, filters

from .models import User, Book, BorrowHistory
from .serializer import UserSerializer, BookSerializer, BorrowHistorySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  filter_fields = ('title', 'publisher', 'author', 'status')

class BorrowHistoryViewSet(viewsets.ModelViewSet):
  queryset = BorrowHistory.objects.all()
  serializer_class = BorrowHistorySerializer
