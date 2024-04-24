from django.test.testcases import TestCase
from .test_Post_Base import PostTestBase
from django.core.exceptions import ValidationError
from recipes.models import Post

class PostCategoryModelTest(PostTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(
            name = 'category test'
            )
        return super().setUp()
    
    def test_post_category_model_string_representation(self):
        self.assertEqual(
            str(self.category),
            self.category.name
        )
    
    #testar o maxlengt
    def test_post_category_model_name_max_length_is_65(self):
        self.category.name = 'A' *66 # vejo aqui se o tamanho respeita os 66 caracteres
        with self.assertRaises(ValidationError): 
            self.category.full_clean()