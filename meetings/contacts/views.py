

from django.shortcuts import render, redirect

from .forms import MyUserRegister
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.urls.base import reverse
from meetings.views import main


def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username', ''),
            password=request.POST.get('password', '')
        )
        if user is not None:
            login(request, user)
            return redirect(reverse(main))
    return render(request, 'login.html', {'form': form})


from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import MyUserRegister

def register_user(request):
    if request.method == 'POST':
        form = MyUserRegister(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            form.save()
            #username = form.get('username')
            #raw_password = form.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('main')
    else:
        form = MyUserRegister()
    return render(request, 'register_user.html', {'form': form})
