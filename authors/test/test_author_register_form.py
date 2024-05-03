from django.test import TestCase
from authors.forms import RegisterForm
from parameterized import parameterized


#teste unitario classico

class AuthorRegisterFormUnitTest():
    # aqui testo logo os parametros todos!!
    @parameterized.expand([
        ('username', 'Your username'),
        ('email', 'Your e-mail'),
        ('first_name', 'Ex.: John'),
        ('last_name', 'Ex.: Doe'),
        ('password', 'Type your password'),
        ('repeat_password', 'Repeat your password'),
    ])

    # vou buscar os parametros que tenho em cima e testo aqui !!
    def test_fields_place_holder(self, field, placeholder):
        form = RegisterForm() # vou buscar o meu register form
        current_placeholder = form[field].field.widget.attrs['placeholder'] # vou ao sitio especifico do meu for e vou buscar o que quero testar
        self.assertEqual(placeholder, placeholder) # testo o value que tenho no placeholder

        #TESTE 2
    @parameterized.expand([
        ('username', (
            'This field is mandatory! 150 characters or less', 
            'Letters, numbers and @/./+/-/_ only.!!')),
        ('email', 'The e-mail must be valid.'),
        ('password', (
            'Password must have at least one uppercase letter,'
            'one lowercase letter and one number. Have length should be'
            'at least 8 characters'
        )),
    ])
    
    def test_fields_help_text(self, field, needed):
        form = RegisterForm()
        current = form[field].field.help_text
        self.assertEqual(current, needed)

    #TESTE3

    @parameterized.expand([
        ('username', 'Username'),
        ('first_name', 'First Name'),
        ('last_name', 'Last Name'),
        ('email', 'E-mail'),
        ('password', 'Password'),
        ('repeat_password', 'repeat_password'),
    ])
    
    def test_fields_label(self, field, needed):
        form = RegisterForm()
        current = form[field].field.label
        self.assertEqual(current, needed)