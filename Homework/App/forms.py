from django import forms
from App.models import User

class Form(forms.Form):
    email    = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class': 'form__block__input', 'name': 'email'}))
    password = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class': 'form__block__input', 'name': 'password'}))
    login    = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class': 'form__block__input', 'name': 'login'}))

class FormEdit(forms.Form):
    lenght = User.objects.count()

    email    = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class': 'form__block__input', 'name': 'email'}))
    password = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class': 'form__block__input', 'name': 'password'}))
    login    = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class': 'form__block__input', 'name': 'login'}))
    index    = forms.IntegerField(required=True, label='', min_value=1, max_value=lenght, widget=forms.NumberInput(attrs={'class': 'form__block__input', 'name': 'index', 'value': 1}))
