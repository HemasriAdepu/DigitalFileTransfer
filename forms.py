# members/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Member

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = []
