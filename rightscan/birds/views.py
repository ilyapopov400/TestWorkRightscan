from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.views import View

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
    """

    def get(self, request, pk=None):
        bird = models.Birds.objects.get(id=pk)
        template_name = "birds/bird-detail.html"
        form_delete = forms.FormDelete()
        context = {"bird": bird,
                   "delete": form_delete}
        return render(request=request, template_name=template_name, context=context)

    def post(self, request, pk=None):
        bird = models.Birds.objects.get(id=pk)
        template_name = "birds/bird-detail.html"
        context = {"bird": bird}
        like = models.Birds.objects.get(id=pk).like + 1
        bird.like = like
        bird.save()

        form_delete = forms.FormDelete(request.POST)
        if form_delete.is_valid():
            if form_delete.cleaned_data.get("delete"):
                bird.delete()
                return render(request=request, template_name="birds/index.html")
        return render(request=request, template_name=template_name, context=context)


class CreateBird(CreateView):
    """
    Создание новой карточки птицы
    """
    form_class = forms.FormBirds
    template_name = "birds/create-bird.html"
    model = models.Birds
    success_url = reverse_lazy('birds:index')


class DeleteBird(DeleteView):
    """
    Удаление карточки птицы
    """
    model = models.Birds
    template_name = 'birds/bird-delete.html'
    success_url = reverse_lazy('birds:index')
    context_object_name = 'bird'
