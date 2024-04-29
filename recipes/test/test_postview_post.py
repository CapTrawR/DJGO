from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from recipes.models import Post
from .test_Post_Base import PostTestBase

#testes unitarios
#class de testes para depois fazer as funcoes
#testar para ver se o home esta a ser passado de views
class PostViewsTest(PostTestBase):
#set up
# testar home View
    def test_post_home_views_is_correct(self):
        view = resolve(reverse('Posts:Home'))
        self.assertIs(view.func, views.home)

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

#testar para ver se a categoria esta a ser bem passada
    def test_post_view_category_is_correct(self):
        view = resolve(reverse('Posts:category', kwargs={'category_id':1}))
        self.assertIs(view.func, views.category)

#testar para ver se a categoria esta a passar status code 404
    def test_post_category_return_status_code_404_if_no_posts(self):
        response = self.client.get(reverse('Posts:category', kwargs={'category_id':1000}))
        self.assertEqual(response.status_code, 404)

#view PostView

#testar para ver se a postview esta a ser passada
    def test_post_view_is_correct(self):
        view = resolve(reverse('Posts:Post', kwargs={'id':1}))
        self.assertIs(view.func, views.postview)

#testar para ver se a categoria esta a passar status code 404
    def test_post_view_return_status_code_404_if_no_posts(self):
        response = self.client.get(reverse('Posts:Post', kwargs={'id':1000}))
        self.assertEqual(response.status_code, 404)




# nao esta a dar para testar as views =/
    def test_post_category_template_dont_load_posts_not_published(self):
        """Test recipe is_published False dont show"""
        # Need a post for this test
        self.make_post()
        response = self.client.get(reverse('Posts:Post', kwargs={'id':1}))
        # Check if one recipe exists
        self.assertEqual(response.status_code, 404)

    def test_post_detail_template_dont_load_post_nt_published(self):
        post = self.make_post(is_published=False)
        response = self.client.get(
            reverse(
                'Posts:Post',
                kwargs={
                    'id': post.id
                }
            )
        )

        self.assertEqual(response.status_code, 404)

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