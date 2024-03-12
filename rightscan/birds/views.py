from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib import messages

from . import models
from . import forms


# Create your views here.

class Index(TemplateView):
    '''
    стартовая страница приложения birds
    '''
    template_name = 'birds/index.html'


class BirdsShow(ListView):
    '''
    Просмотр всех записей в таблице Birds
    '''
    template_name = 'birds/show-all-birds.html'
    model = models.Birds
    context_object_name = 'birds'


class TouchBird(CreateView):
    """
    Создание новой карточки птицы
    """
    template_name = "birds/create-bird.html"
    model = models.Birds
    fields = "__all__"
    success_url = reverse_lazy('birds:index')

    def form_valid(self, form):
        form.save()
        return super(TouchBird, self).form_valid(form)

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     messages.success(self.request, "The task was created successfully.")
    #     return super(TouchBird, self).form_valid(form)
