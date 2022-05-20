from django.test import TestCase

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from account.views import login_user, profile, change_password
from account.models import Profile

# Create your tests here.
class URLTests(SimpleTestCase):
    def test_login(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_user)


class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('bell', 'bell@gmail.com', 'bellpassword')

    def testLogin(self):
        self.client.login(username='bell', password='bellpassword')
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)


