from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.

class Index(TemplateView):
    '''
    стартовая страница приложения birds
    '''
    template_name = 'birds/index.html'
