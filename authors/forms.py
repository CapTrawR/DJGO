from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        #dar outros nomes ao labels
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'E-mail',
            'password': 'Password',
            'username': 'Username',
        }

        help_texts={
            'email': 'The e-mail must be valid!!',
            'username': 'This field is mandatory! 150 characters or less. Letters, numbers and @/./+/-/_ only.!!',
        }

        error_messages={
        'username':{
            'required': 'This field must not be empty!!',
            },
        'email':{
            'required': 'The E-mail must be valid!!',
            },
        'password':{
            'required': 'This field must not be empty!!',
            }
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Type your First Name here',
            }),

            'last_name': forms.TextInput(attrs={
                'placeholder': 'Type your Last Name here'
            }),

            'username': forms.TextInput(attrs={
                'placeholder': 'Type your Username here'
            }),

            'email': forms.TextInput(attrs={
                'placeholder': 'Type your E-mail here'
            }),

            'password': forms.PasswordInput(attrs={
                'placeholder': 'Type your Password here'
            }),

        }