from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from recipes.models import Post
from .test_Post_Base import PostTestBase
from unittest.mock import patch

#testes unitarios
#class de testes para depois fazer as funcoes
#testar para ver se o home esta a ser passado de views
class PostHomeViewTest(PostTestBase):
#set up
# testar home View
    def test_post_home_views_is_correct(self):
        view = resolve(reverse('Posts:Home'))
        self.assertIs(view.func, views.home)
#tearDown

    #testar se a resposta esta ok
    def test_post_home_return_status_code_200_ok(self):
        response = self.client.get(reverse('Posts:Home'))
        self.assertEqual(response.status_code, 200)

#testar se o template usado e o x neste caso
    def test_post_home_view_loads_template_correct(self):
        response = self.client.get(reverse('Posts:Home'))
        self.assertTemplateUsed(response,'recipes/pages/home.html')

#testas se o texto not found aparece
    def test_post_home_shows_no_post_found_if_no_recipes(self):
        Post.objects.get(pk=1).delete()
        response = self.client.get(reverse('Posts:Home'))
        self.assertIn(
            '<h1>No Posts found here 😩😩😩</h1>',
            response.content.decode('utf-8'))
#tenho que escrever mais algumas coisas sobe o test
    #self.fail('Para que eu termine de escrever')

    def test_post_home_template_loads_posts(self):
        response = self.client.get(reverse('Posts:Home')) # executar a url retornou uma resposta 
        response_posts= response.context['posts']
        content = response.content.decode('utf-8') # converter para string
        self.assertIn('Post Title', content)# retorna o conteudo
        self.assertEqual(response_posts.first().title,'Post Title')

    #nao esta a dar 
    def test_post_home_template_dont_load_posts_not_published(self):
        """Test recipe is_published False dont show"""
        # Need a recipe for this test
        self.make_post()
        response = self.client.get(reverse('Posts:Home'))
        # Check if one recipe exists
        self.assertIn(
            '<h1>No Posts found here 😩😩😩 </h1>',
            response.content.decode('utf-8')
        )

    def test_post_home_is_paginated(self):
        for i in range(9):
            kwargs = {'slug': f'r{i}', 'author_data': {'username': f'u{i}'}}
            self.make_post(**kwargs)
                
        with patch('posts.views.PER_PAGE', new=3):
            response = self.client.get(reverse('Posts:Home'))
            posts = response.context['posts']
            paginator = posts.paginator

            self.assertEqual(paginator.num_pages, 3)
            self.assertEqual(len(paginator.get_page(1)), 3)
            self.assertEqual(len(paginator.get_page(2)), 3)
            self.assertEqual(len(paginator.get_page(3)), 2)

    # para ver se a view chama pagination incorrecta        
    def test_invalid_page_query_uses_page_one(self):
        for i in range(8):
            kwargs = {'slug': f'r{i}', 'author_data': {'username': f'u{i}'}}
            self.make_post(**kwargs)

        with patch('posts.views.PER_PAGE', new=3):
            response = self.client.get(reverse('Posts:Home') + '?page=12A')
            self.assertEqual(
                response.context['posts'].number,
                1
            )
            response = self.client.get(reverse('Posts:Home') + '?page=2')
            self.assertEqual(
                response.context['posts'].number,
                2
            )
            response = self.client.get(reverse('Posts:Home') + '?page=3')
            self.assertEqual(
                response.context['posts'].number,
                3
            )