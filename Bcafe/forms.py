# forms.py
from django import forms
from .models import Mycoffee

class MycoffeeForm(forms.ModelForm):
    class Meta:
        model = Mycoffee
        fields = ['name', 'price', 'image', 'image_url']  # Mycoffee/models.py