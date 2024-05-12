from django import forms
from .models import Account, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ismingizni kiriting',
        'class': 'form-control',

    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Familiyangizni kiriting',
        'class': 'form-control'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Pochta manzilingizni kiriting',
        'class': 'form-control',
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Foydalanuvchi nomini kiriting',
        'class': 'form-control'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email',
                  'username', 'password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError(
                'password dose not match',

            )


class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '',
        'class': 'form-control'
    }))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder': '',
        'class': 'form-control'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number']


class UserProfileForm(forms.ModelForm):
    address_line_1 = forms.CharField(widget=forms.TextInput(attrs={

        'class': 'form-control',

    }))

    address_line_2 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '',
        'class': 'form-control'
    }))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={

        'class': 'form-control'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={

        'class': 'form-control'

    }))

    city = forms.CharField(widget=forms.TextInput(attrs={

        'class': 'form-control'
    }))
    country = forms.CharField(widget=forms.TextInput(attrs={

        'class': 'form-control'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={

        'class': 'form-control',

    }))

    state = forms.CharField(widget=forms.TextInput(attrs={

        'class': 'form-control'
    }))
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={

        'class': 'form-control'
    }))

    class Meta:
        model = UserProfile
        fields = ['address_line_1', 'address_line_2', 'city', 'country', 'state', 'profile_pic']
