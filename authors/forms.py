import re

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()

def add_placeholder(field, placeholder_val):
    add_attr(field,'placeholder', placeholder_val)

# defenir os characters a ser usados na pw!
def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError(
            'Password must have at least one uppercase letter,'
            'one lowercase letter and one number. Have length should be'
            'at least 8 characters'
        )
    code='invalid'
class RegisterForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Your Username')
        add_placeholder(self.fields['email'], 'Your e-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: John')
        add_placeholder(self.fields['last_name'], 'Ex.: Doe')
        add_placeholder(self.fields['password'], 'Type your password')
        add_placeholder(self.fields['repeat_password'], 'Repeat your password')
        add_attr(self.fields['username'], 'css', 'a-css-class')
   
    username = forms.CharField(
        required=True,
        label='Username',
        help_text='This field is mandatory! 150 characters or less' 
            'Letters, numbers and @/./+/-/_ only.!!',
        error_messages={
            'required': 'This field must not be empty!!',
            'min_length': 'Username must have at least 4 character',
            'max_length': 'Username must have less then 150 characters',
        },
        min_length=4, max_length=150,
   )
    first_name = forms.CharField(
        error_messages={'required':'Write your first name'},
        required=True,
        label='First Name'
   )
    last_name = forms.CharField(
       error_messages={'required':'Write your last name'},
       required=True,
       label='Last Name'
   )
    email = forms.EmailField(
       error_messages={'required':'Email must be valid.'},
       required=True,
       label='E-mail',
       help_text='The e-mail must be valid.',
   )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        error_messages={
             'required': 'This field must not be empty!!',
        },
        help_text=(
            'Password must have at least one uppercase letter,'
            'one lowercase letter and one number. Have length should be'
            'at least 8 characters'
        ),

        validators=[strong_password], # aqui obrigo a usar a funcao com o regex 
        label='Password',
    )
    repeat_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        label='Repeat Password',
        error_messages={
             'required': 'This field must not be empty!!',
        },
    )
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        # widgets = {
        #     'first_name': forms.TextInput(attrs={
        #         'placeholder': 'Type your First Name here',
        #     }),

        #     'last_name': forms.TextInput(attrs={
        #         'placeholder': 'Type your Last Name here'
        #     }),

        #     'username': forms.TextInput(attrs={
        #         'placeholder': 'Type your Username here'
        #     }),

        #     'email': forms.TextInput(attrs={
        #         'placeholder': 'Type your E-mail here'
        #     }),

        #     'password': forms.PasswordInput(attrs={
        #         'placeholder': 'Type your Password here'
        #     }),

       # }
    
#metodo clean para validar o formulario como um todo quando um depende do outro
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')

        #quero que o erro apareca no pw entao faço um dicionario e levo o erro em atrelado
        if password != repeat_password:
            password_confirmation_error = ValidationError(
                'Password and Repeat Password must be equal',
                code = 'invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                #isto pode ir aqui como exemplo a dizer que podemos meter isto numa lista!
                'repeat_password':[
                    password_confirmation_error,
                ]
            })
    