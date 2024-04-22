from django.test import TestCase
from django.urls import reverse


class PostURLsTest(TestCase):
    def test_the_pytest_is_ok (self):
        ...

    def test_UrlHome_is_correct(self):
        home_url = reverse('Posts:Home')
        self.assertEqual(home_url,'/')

    def test_Url_is_correct(self):
        url = reverse('Posts:category', kwargs={'category_id' : 1})
        self.assertEqual(url,'/Posts/category/1/')

    def test_UrlPost_is_correct(self):
        url = reverse('Posts:Post', kwargs={'id':1})
        self.assertEqual(url,'/Posts/1/')