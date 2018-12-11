from django.contrib import admin
from .models import User, Book, BorrowHistory

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  pass

@admin.register(Book)
class Book(admin.ModelAdmin):
  pass

@admin.register(BorrowHistory)
class BorrowHItory(admin.ModelAdmin):
  pass
