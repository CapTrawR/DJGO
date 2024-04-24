from django.test.testcases import TestCase
from .test_Post_Base import PostTestBase
from django.core.exceptions import ValidationError
from parameterized import parameterized
from recipes.models import Post

class PostModelTest(PostTestBase):
    def setUp(self) -> None:
        self.post = self.make_post()
        return super().setUp()
    
    # data para fazer teste ao post
    def make_post_no_defaults(self):
        post = Post(
            category_data = self.make_category(name='teste default category'),
            author_data = self.make_author(username='UserNew'),
            title = 'Post Title',
            description = 'Post Description',
            slug = 'Post-Slug',
            speciality = 'speciality',
            post_field = 'postfield',    
        )
        post.full_clean()
        post.save()
        return post

    @parameterized.expand([
        ('title', 65),
        ('description', 165),
        ('speciality', 65),
        ('post_field', 3000),
    ])

    def test_post_fileds_max_lenght(self, field, max_length):
        setattr(self.post, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.post.full_clean()

    def test_post_presentation_field_is_html_is_false_by_default(self):
        post = self.make_post_no_defaults()
        self.assertFalse(post.post_field_is_html, msg='Post field is html is not false')

    def test_post_is_published_is_false_by_default(self):
        post = self.make_post_no_defaults()
        self.assertFalse( post.is_published, msg='Post field is published false')