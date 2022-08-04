from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import  AuthenticationForm


User = get_user_model()


class RegistrationForm(forms.ModelForm):

    full_name = forms.CharField(
        max_length=20, 
        required=False,
        label='Full Name',
        widget=forms.TextInput(
            attrs={
                'class': 'uk-input mb-2 fw-bold',
                }))

    username = forms.CharField(
        required=False,
        label='Username',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'uk-input mb-2 fw-bold'
                }))
    
    phone_number = forms.CharField(
        max_length=10,
        required=False,
        label='Phone Number',
        widget=forms.TextInput(
            attrs={
                'class': 'uk-input mb-2 fw-bold'
                }))

    address = forms.CharField(
        max_length=100,
        required=False,
        label='Address',
        widget=forms.TextInput(
            attrs={
                'class': 'uk-input mb-2 fw-bold'
                }))

    email = forms.EmailField(
        required=False,
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'uk-input mb-2 fw-bold'
                }))

    password1 = forms.CharField(
        required=False,
        label='Password',
        max_length=20,
        widget=forms.PasswordInput(
                attrs={
                'class': 'uk-input mb-2 fw-bold',
                'autocomplete': 'new-password'
                }))

    password2 = forms.CharField(
        required=False,
        label='Confirm Password',
        max_length=20,
        widget=forms.PasswordInput(
                attrs={
                'class': 'uk-input mb-2 fw-bold'
                }))

    class Meta:
        model = User
        fields = (
            'full_name',
            'username',
            'phone_number',
            'address',
            'email',
            'password1',
            'password2',
        )

class MyLoginForm(AuthenticationForm):
    def __init__(self, request, *args, **kwargs):
        # simply do not pass 'request' to the parent
        super().__init__(*args, **kwargs)
    
    username = forms.EmailField(
        required=False,
        label='Email',
        widget=forms.TextInput(
            attrs={
                'class': 'uk-input mb-2 fw-bold',
                'required': 'false'
                },
                
                ))

    password = forms.CharField(
        required=False,
        label='Password',
        max_length=20,
        widget=forms.PasswordInput(
                attrs={
                'class': 'uk-input mb-2 fw-bold',
                'autocomplete': 'current-password'
                }))
