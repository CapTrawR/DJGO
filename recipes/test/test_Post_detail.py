from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from recipes.models import Post
from .test_Post_Base import PostTestBase

#testes unitarios
#class de testes para depois fazer as funcoes
#testar para ver se o home esta a ser passado de views
class PostDetailViewsTest(PostTestBase):
#view PostView

#testar para ver se a postview esta a ser passada
    def test_post_view_is_correct(self):
        view = resolve(reverse('Posts:Post', kwargs={'id':1}))
        self.assertIs(view.func, views.postview)


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

    def test_post_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('Posts:Post', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    
    def test_post_detail_template_loads_the_correct_post(self):
        needed_title = 'This is a detail page - It load one post'

        # Need a recipe for this test
        self.make_post(title=needed_title)

        response = self.client.get(
        reverse(
            'Posts:Post',
            kwargs={
                'id': 1
            }
        )
    )
        content = response.content.decode('utf-8')
