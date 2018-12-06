# coding: utf-8

from rest_framework import serializers

from .models import User, Book

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publisher', 'image_url', 'status', 'updated_at', 'created_at')
