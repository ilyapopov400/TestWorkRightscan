from django.urls import path
from . import views

app_name = 'birds'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),  # просмотр главной страницы
    path('birds/', views.BirdsShow.as_view(), name='show-all-birds'),  # просмотр всех птиц
    path('birds/<int:pk>', views.OneBird.as_view(), name='one-bird-detail'),  # просмотр одной птицы
    path('birds/create', views.CreateBird.as_view(), name='create-bird'),  # создание новой карточки для птицы
]
