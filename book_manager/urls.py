# coding: utf-8

from rest_framework import routers
from .views import UserViewSet, BookViewSet, BorrowHistoryViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'borrowhistories', BorrowHistoryViewSet)
