from django import forms
from django.contrib.auth.models import User
from .models import reg

class regForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','password')
        widgets = {
        'password':forms.PasswordInput(attrs={'type':'password'})
        }

class regform1(forms.ModelForm):
    class Meta:
        model = reg
        fields = ('contact',)
