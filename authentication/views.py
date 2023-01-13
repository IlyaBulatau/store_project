from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.urls import reverse_lazy

from authentication.forms import UserLoginForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse_lazy('home'))
    else:
        form = UserLoginForm()
        context = {'form': form }
    return render(request, 'authentication/login.html', context)

def register(request):
    pass
