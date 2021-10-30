from django.views import View
from django.shortcuts import render
from .forms import SignUpForm
from django.views.generic.list import ListView
from .models import User, Follow
from django.http import HttpResponseRedirect
from django.urls import reverse

PASSWORD_MINIMUM_LENGTH = 8

# 회원가입View

from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user_instance=signup_form.save(commit=False)
            user_instance.set_password(signup_form.cleaned_data['password'])
            user_instance.save()
            return render(request, 'user/signup_complete.html', {'username': user_instance.username})
        else:
            signup_form = SignUpForm()
        return render(request, 'user/signup.html', {'form':signup_form.as_p})


