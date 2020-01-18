from django import forms
from django.contrib.auth.models import AbstractUser
from .models import Fanfic


class UserForm(forms.ModelForm):
    class Meta:
        model = AbstractUser
        fields = ('username',)

class FanficForm(forms.ModelForm):
    class Meta:
        model = Fanfic
        fields = ('title', 'text', 'image', 'genre', 'tags', )
