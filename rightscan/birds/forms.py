from django import forms
from . models import Birds


class FormBirds(forms.ModelForm):
    class Meta:
        model = Birds
        fields = ('name', 'color', 'image')
