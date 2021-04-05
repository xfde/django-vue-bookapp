# bookstore/urls.py
from django.urls import include, path
from rest_framework import routers
from django.conf.urls import url
from . import views
from django.views.static import serve
from .views import signup, isLoggedin, signout, signin, add_favourites, list_favourites, remove_favourite_book, add_book
router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/',signup),
    path('checklogin/',isLoggedin),
    path('logout/',signout),
    path('login/',signin),
    path('addfavourites/',add_favourites),
    path('listfavorites/',list_favourites),
    path('removefavourites/', remove_favourite_book),
    path('addbook/',add_book)
]

