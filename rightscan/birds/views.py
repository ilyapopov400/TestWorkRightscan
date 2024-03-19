from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
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


class OneBird(View):
    """
    Показ одной птицы
    Проставление лайка птице
    и возможность ее удалить - не реализованно
    """

    def get(self, request, pk=None):
        bird = models.Birds.objects.get(id=pk)
        template_name = "birds/bird-detail.html"
        context = {"bird": bird}
        return render(request=request, template_name=template_name, context=context)

    def post(self, request, pk=None):
        bird = models.Birds.objects.get(id=pk)
        template_name = "birds/bird-detail.html"
        context = {"bird": bird}
        like = models.Birds.objects.get(id=pk).like + 1
        bird.like = like
        bird.save()
        return render(request=request, template_name=template_name, context=context)


class CreateBird(CreateView):
    """
    Создание новой карточки птицы
    """
    form_class = forms.FormBirds
    template_name = "birds/create-bird.html"
    model = models.Birds
    # fields = ["name", "color", "image"]
    success_url = reverse_lazy('birds:index')

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     messages.success(self.request, "The task was created successfully.")
    #     return super(TouchBird, self).form_valid(form)


class DeleteBird(DeleteView):
    """
    Удаление карточки птицы
    """
    model = models.Birds
    template_name = 'birds/bird-delete.html'
    success_url = reverse_lazy('birds:index')
    context_object_name = 'bird'
