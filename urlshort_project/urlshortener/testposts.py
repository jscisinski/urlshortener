from django.test import TestCase
from django.test.client import RequestFactory

from urlshort.urlshortener import redirect_url_view, Shortener


class PostTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_details(self):
        post = Shortener(long_url='https://www.docker.com/get-started/')
        post.save()
        self.assertEqual(post.long_url, "https://www.docker.com/get-started/")
        request = self.factory.get('')
        response = redirect_url_view(request, post.short_url)
        #302 - found and redirected
        self.assertEqual(response.status_code, 302)
