from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from recipes.models import Post
from .test_Post_Base import PostTestBase

#testes unitarios
#class de testes para depois fazer as funcoes
#testar para ver se o home esta a ser passado de views
class PostSearchViewsTest(PostTestBase):

    # para ver se passa o url
    def test_post_search_uses_correct_view_function(self):
        resolved = resolve(reverse('Posts:search'))
        self.assertIs(resolved.func, views.search)

    # para ver se carrega o template direito
    def test_post_search_loads_correct_template(self):
        response = self.client.get(reverse('Posts:search') +'?q=teste')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    #aqui vemos se da erro 404
    def test_recipe_serach_raises_404_if_no_search(self):
        response = self.client.get(reverse('Posts:search'))
        self.assertEqual(response.status_code, 404)

    def test_post_search_raises_404_if_no_search_term(self):
        url = reverse('Posts:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_post_search_term_is_on_page_title_and_escaped(self):
        url = reverse('Posts:search') + '?q=<Teste>'
        response = self.client.get(url)
        self.assertIn(
            'Search for &quot;&lt;Teste&gt;&quot;',
            response.content.decode('utf-8'))
        
    def test_post_search_term_can_find_test(self):
        title1 = 'This is post one'
        title2 = 'This is post 2'

        post1  = self.make_post(
            slug ='one',
            title=(title1),
            author_data={'username':'one'},
        )

        post2  = self.make_post(
            slug ='two',
            title=(title2),
            author_data={'username':'two'},
        )
        search_url = reverse ('Posts:search'),
        response1 = self.client.get(f'{search_url} ?q={title1}'),
        response2 = self.client.get(f'{search_url} ?q={title2}'),
        response_both = self.client.get(f'{search_url} ?q=this'),

        self.assertIn(post1, response1.context['Posts'])
        self.assertIn(post2, response2.content ['Posts'])
        self.assertIn(post1, post2, response_both.content ['Posts'])
    
    