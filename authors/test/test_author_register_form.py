from django.test import TestCase
from django.test import TestCase as DjangoTestCase
from authors.forms import RegisterForm
from parameterized import parameterized
from django.urls import reverse


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
            'This field is mandatory! 150 characters or less'
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

class AuthorRegisterFormIntegrationTest(DjangoTestCase):
    def setUp(self, *args, **kwargs) -> None:
        # validar o usuario
        self.form_data = {
        'username': 'user',
        'first_name': 'First',
        'last_name': 'Last',
        'email': 'email@email.com',
        'password': 'Abc12345678',
        'repeat_password': 'Abc12345678',
        }
        return super().setUp(*args, **kwargs)
    
    @parameterized.expand([
        ('username', 'this field must not be empty.'),
        ('first_name', 'Write your first name.'),
        ('last_name', 'Write your last name.'),
        ('e-mail', 'Email must be valid'),
        ('password', 'This field must not be empty.'),
        ('repeat_password', 'This field must not be empty.'),
    ])
    # os campos nao podem ser vazios:
    def test_fields_cannot_be_empty(self, field, msg):
        self.form_data[field] = '' # field e = a um valor vazio
        url = reverse('authors:register_create')
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get(field))

    #testar o tamanho do usuario:
    def test_username_field_min_length_should_be_4(self,username):
        self.form_data[username] = 'Joao' # field e = a um valor vazio
        url = reverse('authors:register_create')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'Username must have at least 4 character'
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get(username))

    #testar o tamanho do usuario:
    def test_username_field_max_length_should_be_150(self,username):
        self.form_data[username] = 'Joao' *151 # field e = a um valor vazio
        url = reverse('authors:register_create')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'Username must have less then 150 characters'
        self.assertIn(msg, response.context['form'].errors.get(username))
        self.assertIn(msg, response.content.decode('utf-8'))
    
    #testar a strong password
    def test_passwrod_field_have_uper_lower_case_letter_and_numbers(self,password):
        self.form_data[password] = '@Abc1234' # password a ser passada para gerar erro
        url = reverse('authors:register_create')
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = 'Password must have at least one uppercase letter,'
        'one lowercase letter and one number. Have length should be'
        'at least 8 characters',
        
        self.assertIn(msg, response.context['form'].errors.get(password))
        self.assertIn(msg, response.content.decode('utf-8'))

        self.form_data['password'] = '@A123abc123'
        url = reverse('authors:register_create')
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertNotIn(msg, response.context['form'].errors.get('password'))

    #ver se as pw sao iguais ou nao
    def test_password_and_password_confirmation_are_equal(self):
        self.form_data['password'] = '@A123abc123'
        self.form_data['repeat_password'] = '@A123abc1235'

        url = reverse('authors:register_create')
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = 'Password and Repeat Password must be equal'

        self.assertIn(msg, response.context['form'].errors.get('password'))
        self.assertIn(msg, response.content.decode('utf-8'))

        self.form_data['password'] = '@A123abc123'
        self.form_data['repeat_password'] = '@A123abc123'

        url = reverse('authors:register_create')
        response = self.client.post(url, data=self.form_data, follow=True)

        self.assertNotIn(msg, response.content.decode('utf-8'))
    
    # ver se retorna a 404
    def test_send_get_request_to_registration_create_view_returns_404(self):
        url = reverse('authors:register_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    #ver se o email e unico
    def test_email_field_must_be_unique(self):
        url = reverse('authors:register_create')

        self.client.post(url, data=self.form_data, follow=True)
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = 'User e-mail is already in use'
        self.assertIn(msg, response.context['form'].errors.get('email'))
        self.assertIn(msg, response.content.decode('utf-8'))

    # usuario pdoe logar
    def test_user_can_log_in(self):
        url = reverse ('authors:register_create')

        self.form_data.update({
            'username':'testuser',
            'password':'Abc123456',
            'repeat_password':'Abc123456',
        })

        self.client.post(url, data=self.form_data,follow=True)

        is_authenticated = self.client.login(
            username='testuser',
            password = 'Abc123456',
        )
        
        self.assertTrue(is_authenticated)