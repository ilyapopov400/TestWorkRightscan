from django.urls import path
from . import views

app_name = 'birds'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),  # просмотр главной страницы
]
