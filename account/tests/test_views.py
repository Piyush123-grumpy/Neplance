from django.test import TestCase,Client
from django.urls import reverse


class Test_views(TestCase):
    def test_signin(self):
        client=Client()
        response=client.get(reverse('signin'))
        # self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'account/login.html')
    
    def test_usersignup(self):
        client=Client()
        response=client.get(reverse('signup'))
        self.assertTemplateUsed(response,'account/signup.html')
