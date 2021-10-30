from django.contrib.auth.models import User
from django import forms

class SignUpForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','password','first_name','last_name','email']