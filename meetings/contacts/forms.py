'''
from django import forms
from .models import *



class CheckoutContactForm(forms.Form):
    username = forms.CharField(required=True)
    username = forms.PassField(required=True)
    #phone = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = models.EmailField(required=True)
'''
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class MyUserRegister(UserCreationForm):


    class Meta:
        model = MyUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )