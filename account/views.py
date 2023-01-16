from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from account import forms


def profile(request):
    if request.method=='POST':
        form = forms.ProfileForm( instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = forms.ProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'account/profile.html', context)


