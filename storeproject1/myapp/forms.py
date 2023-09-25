from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField,AuthenticationForm
from django.contrib.auth.models import User

from .models import Form


class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))




class CustomerRegistrationForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model=User
        fields=['username','password1','password2']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = '__all__'