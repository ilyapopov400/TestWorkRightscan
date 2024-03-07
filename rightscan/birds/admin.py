from django.contrib import admin

# Register your models here.

from . import models


class BirdsAdmin(admin.ModelAdmin):
    list_display = ["name", "color", "image", ]


admin.site.register(models.Birds)
