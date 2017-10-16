from django import forms
from django.forms import ModelForm
from .models import *
from datetime import datetime


now = datetime.now().strftime('%d.%m.%Y')


class RequestForm(ModelForm):
    name = forms.CharField(max_length=20,
                           label='Имя',
                           widget=forms.TextInput(attrs={'placeholder': 'Василий', 'class': 'form-control'})
                           )
    surname = forms.CharField(max_length=20,
                              label='Фамилия',
                              widget=forms.TextInput(attrs={'placeholder': 'Пупкин', 'class': 'form-control'})
                              )
    email = forms.EmailField(label='email',
                             widget=forms.EmailInput(attrs={'placeholder': 'pupkin@mail.ru', 'class': 'form-control'})
                             )
    phone = forms.CharField(max_length=12,
                            label='Телефон',
                            widget=forms.TextInput(attrs={'placeholder': '+79001234567', 'class': 'form-control'})
                            )
    date = forms.DateField(label='Желаемая дата',
                           widget=forms.DateInput(attrs={'placeholder': now, 'class': 'form-control'}),
                           input_formats=['%d.%m.%Y']
                           )

    class Meta:
        model = Request
        fields = '__all__'
        # fields = ['name', 'surname', 'email', 'phone']
