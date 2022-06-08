from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from .views import addgigs

# Create your tests here.

# URL Testing for add gig.
class TestAddgigURL(SimpleTestCase):
    def test_home_url2(self):
        url=reverse('addgig')
        print(url)
        self.assertEqual(resolve(url).func,addgigs)

