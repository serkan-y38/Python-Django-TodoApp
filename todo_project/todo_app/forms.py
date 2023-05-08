from django import forms
from django.forms import fields
from .models import Todos


class Listform(forms.ModelForm):
    class Meta:
        model = Todos
        fields = ['description', 'title', 'date', 'finished']
