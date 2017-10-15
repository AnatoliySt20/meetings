from django.shortcuts import render
from contacts.models import MyUser
from .models import *
from .forms import *
print('xhi3')



def event(request):
    events = Event.objects.filter(is_active=True)
    users = MyUser.objects.filter(is_active=True)

    return render(request, 'events.html', locals())

def register_event(request):
    form = MakeEventForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        data  = form.cleaned_data
        new_form = form.save()
    return render(request, 'register_event.html', locals())
