from django.test import Client, SimpleTestCase, TestCase
from django.urls import resolve, reverse
from account.models import User, UserManager

from account.views import loginpage, register


class URLTests(SimpleTestCase):
    def test_login(self):
        url = reverse('login_dashboard')
        self.assertEquals(resolve(url).func, loginpage)

    def test_register(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)


class TestModels(TestCase):
    def setUp(self):
        self.profile1 = User.objects.create(
            username = 'Profile 1',
            email = 'pooja@gmail.com'

        )
    def test_profile_model(self):
        self.assertEquals(self.profile1.username, 'Profile 1')



class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('bell', 'bell@gmail.com', 'bellpassword')

    def testLogin(self):
        self.client.login(username='bell', password='bellpassword')
        response = self.client.get(reverse('login_dashboard'))
        self.assertEqual(response.status_code, 302)