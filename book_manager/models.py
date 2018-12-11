import datetime
from django.db import models
from django.utils import timezone

BOOK_STATUSES = (
    (1, 'unborrowed'),
    (2, 'borrowed'),
)

BORROW_STATUSES = (
    (1, 'borrow'),
    (2, 'return'),
)

class User(models.Model):
  name = models.CharField(max_length=32)
  mail = models.EmailField()

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=200)
  publisher = models.CharField(max_length=200) 
  image_url = models.URLField(max_length=200, null=True)
  status = models.IntegerField(choices=BOOK_STATUSES)
  updated_at = models.DateTimeField(auto_now=True) 
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

  def is_borrowed(self):
    return self.status == 2

  def borrow_book(self):
    self.status = 2
    self.save()
    return 2

  def return_book(self):
    self.status = 1
    self.save()
    return 1

class BorrowHistory(models.Model):
  user = models.ForeignKey(User, related_name='borrow_history', on_delete=models.CASCADE)
  book = models.ForeignKey(Book, related_name='entries', on_delete=models.CASCADE)
  status = models.IntegerField(choices=BORROW_STATUSES)
  updated_at = models.DateTimeField(auto_now=True) 
  created_at = models.DateTimeField(auto_now_add=True)
