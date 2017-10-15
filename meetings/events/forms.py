from django import forms
from .models import *



class MakeEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['address', 'description']

