from django import forms
from django.forms import ModelForm
from .models import *


class RequestForm(ModelForm):
    name = forms.CharField(max_length=20,
                           label='Имя',
                           widget=forms.TextInput(attrs={'placeholder': 'Василий'})
                           )
    surname = forms.CharField(max_length=20,
                              label='Фамилия',
                              widget=forms.TextInput(attrs={'placeholder': 'Пупкин'})
                              )
    email = forms.EmailField(label='email',
                             widget=forms.EmailInput(attrs={'placeholder': 'pupkin@mail.ru'})
                             )
    phone = forms.CharField(max_length=12,
                            label='Телефон',
                            widget=forms.TextInput(attrs={'placeholder': '+79001234567'})
                            )
    date = forms.DateField(label='Желаемая дата',
                           # widget=forms.DateInput(),
                           input_formats=['%d.%m.%Y']
                           )

    class Meta:
        model = Request
        fields = '__all__'
        # fields = ['name', 'surname', 'email', 'phone']
