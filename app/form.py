from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django import forms

from .models import Cards


class OrderForm(ModelForm):
    class Meta:
        model = Cards
        fields = '__all__'


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
