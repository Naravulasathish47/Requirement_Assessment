from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    email = forms.EmailField(max_length=200)
    UserName = forms.CharField(max_length=200)
    Date_of_Birth = forms.DateField()
    Address = forms.CharField(max_length=2000, label='Address')
    Phone = forms.IntegerField()
    FirstName = forms.CharField(max_length=200, label='First Name')
    LastName = forms.CharField(max_length=200, label='Last Name')

    class Meta:
        model = Profile
        fields = ['email', 'UserName', 'Date_of_Birth', 'Address', 'Phone', 'FirstName', 'LastName']