from django.test import TestCase
from recipes.models import Category, Post, User

class PostTestBase(TestCase):
    def setUp(self) -> None:
        self.make_post()
        return super().setUp()
    
    #funcoes para carregar no set up
    def make_category(self,name='category'):
        return Category.objects.create(name = name)
    
    def make_author(self,
            first_name = "user",
            last_name = "name",
            username="username",
            password="123456",
            email="username@gmail.com",   ):
        return User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password,
            email= email,
        )
    
    def make_post(
        self,
        category_data = None,
        author_data = None,
        title = 'Post Title',
        description = 'Post Description',
        slug = 'Post Slug',
        first_name = 'firstname',
        last_name = 'lastname',
        speciality = 'speciality',
        post_field = 'postfield',
        post_field_is_html = False,
        created_at = 'criado a ',
        updated_at = 'update at',
        is_published = True,
    ):
        if category_data is None:
            category_data = {}
        
        if author_data is None:
            author_data ={}

        return Post.objects.create(
        category = self.make_category(**category_data), # vai buscar tudo o que esta dentro do dicionario
        author = self.make_author(**author_data),# vai buscar tudo o que esta dentro do dicionario
        title = title,
        description = description,
        slug = slug ,
        first_name = first_name,
        last_name = last_name,
        speciality = speciality,
        post_field = post_field ,
        post_field_is_html = post_field_is_html,
        created_at = created_at,
        updated_at = updated_at,
        is_published = is_published ,
        )
        