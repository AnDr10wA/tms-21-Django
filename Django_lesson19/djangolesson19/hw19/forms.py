from django import forms
from django.forms import ModelForm
from .models import Aviaticket
class Aviaticketform(ModelForm):
    class Meta:
        model = Aviaticket
        fields = ['name', 'from_him', 'where_him', 'what', 'date']


