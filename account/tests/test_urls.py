# from signal import SIGINFO
# from typing_extensions import Self
# from urllib.parse import urlparse
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from account.views import *

class TestUrls(SimpleTestCase):
      def test_signin_urls_is_resolved(self):
        url=reverse('signin')
        view=resolve(url).func
        Self.assertEquals(view,SIGINFO)

      def test_usersignup_urls_is_resolved(self):
        url=reverse('usersignup')
        view=resolve(url).func
        self.assertEquals(view,userSignup)