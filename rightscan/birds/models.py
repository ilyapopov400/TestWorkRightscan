from django.db import models
import os
import rightscan.settings


# Create your models here.

class Birds(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя птицы")
    color = models.CharField(max_length=20, verbose_name="Цвет птицы")
    like = models.IntegerField(default=0, verbose_name="Лайки, поставленные птице")
    image = models.ImageField(upload_to='images', verbose_name="Изображение птицы")

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):  # удаление файла при удалении карточки птицы
        result = super(Birds, self).delete()
        os.remove("{}/{}".format(rightscan.settings.MEDIA_ROOT, self.image))
        return result
