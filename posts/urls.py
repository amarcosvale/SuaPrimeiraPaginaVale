from django.urls import path
from .views import home, create_author, create_category, create_post, search_post

urlpatterns = [
    path('', home, name='home'),
    path('create-author/', create_author, name='create_author'),
    path('create-category/', create_category, name='create_category'),
    path('create-post/', create_post, name='create_post'),
    path('search/', search_post, name='search_post'),
]
