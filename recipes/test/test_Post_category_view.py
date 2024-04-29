from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from recipes.models import Post
from .test_Post_Base import PostTestBase

#testes unitarios
#testar para ver se a categoria esta a ser bem passada das views
class PostCategoryViewsTest(PostTestBase):
#testar para ver se a categoria esta a ser bem passada
    def test_post_view_category_is_correct(self):
        view = resolve(reverse('Posts:category', kwargs={'category_id':1}))
        self.assertIs(view.func, views.category)

#testar para ver se a categoria esta a passar status code 404
    def test_post_category_return_status_code_404_if_no_posts(self):
        response = self.client.get(reverse('Posts:category', kwargs={'category_id':1000}))
        self.assertEqual(response.status_code, 404)


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


