from django import forms
from .models import Order


class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'css_input'}))
    phone = forms.CharField(max_length=200)
