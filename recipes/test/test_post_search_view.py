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