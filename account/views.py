from django.shortcuts import render

from account import forms


def profile(requsest):
    form = forms.ProfileForm()
    context = {'form': form}
    return render(requsest, 'account/profile.html', context)


