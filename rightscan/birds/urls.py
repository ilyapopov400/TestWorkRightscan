from django.urls import path
from . import views

app_name = 'birds'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),  # просмотр главной страницы
    path('show-all/', views.BirdsShow.as_view(), name='show-all-birds'),  # просмотр всех птиц
    path('create-bird/', views.TouchBird.as_view(), name='create-bird'),  # создание новой карточки для птицы
]
