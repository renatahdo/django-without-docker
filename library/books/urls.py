from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'author', views.AuthorViewSet)
router.register(r'genre', views.GenreViewSet)
router.register(r'language', views.LanguageViewSet)
router.register(r'booksauthor', views.BooksAuthorsViewSet)
router.register(r'booksauthor', views.BooksAuthorsViewSet)
router.register(r'booksgenre', views.BooksGenresViewSet)
router.register(r'bookslanguage', views.BooksLanguagesViewSet)
router.register(r'', views.BookViewSet)

urlpatterns = [
	path('', include(router.urls)),
]