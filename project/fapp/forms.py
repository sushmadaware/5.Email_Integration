from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class SignupForm(UserCreationForm):
    email=forms.EmailField(max_length=200,help_text='Required')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = forms.CharField(validators=[phone_regex], max_length=17)

    class Meta:
        model = User
        fields = ['username', 'email','password1','password2','phone']