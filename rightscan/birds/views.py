from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from . import models


# Create your views here.

class Index(TemplateView):
    '''
    стартовая страница приложения birds
    '''
    template_name = 'birds/index.html'


class BirdsShow(ListView):
    '''
    просмотр всех записей в таблице Birds
    '''
    template_name = 'birds/show-all-birds.html'
    model = models.Birds
    context_object_name = 'birds'
