
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


def log_out(request):
    logout(request)
    return redirect(reverse('login'))
