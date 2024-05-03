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
    def test_first_name_place_holder_is_correct(self, field, placeholder):
        form = RegisterForm() # vou buscar o meu register form
        current_placeholder = form[field].field.widget.attrs['placeholder'] # vou ao sitio especifico do meu for e vou buscar o que quero testar
        self.assertEqual(placeholder, placeholder) # testo o value que tenho no placeholder