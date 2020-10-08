from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm    # django inbuilt  Registration form
from .models import Profile

class UserRegisterForm(UserCreationForm):   # uses UserCreationForm
    email = forms.EmailField()

    class Meta:     # UserCreationForm doesn't have email field, we add here with other fields.
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Form in which User can update Username & email.
class UserUpdateForm(forms.ModelForm):     
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# Form to Update image of Profile model.
class ProfileUpdateForm(forms.ModelForm):     
    class Meta:
        model = Profile
        fields = ['image']
