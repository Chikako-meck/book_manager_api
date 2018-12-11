# coding: utf-8

from rest_framework import serializers

from .models import User, Book, BorrowHistory

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publisher', 'image_url', 'status', 'updated_at', 'created_at')

class BorrowHistorySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    book = BookSerializer()
    class Meta:
        model = BorrowHistory
        fields = ('user', 'book', 'status', 'updated_at', 'created_at')
