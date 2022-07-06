from distutils.core import setup
import json
from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from .views import addgigs
from .models import Category, Gig
from account.models import User, Employer, Freelancer
import requests
# Create your tests here.

# URL Testing for add gig.
# class TestAddgigURL(SimpleTestCase):
#     def test_home_url2(self):
#         url=reverse('addgig')
#         print(url)
#         self.assertEqual(resolve(url).func,addgigs)

class JobDetailUnitTestCase(TestCase):

    def createUser(self):
        user = User.objects.create(username='testuser', password='testpass', email='testuser123@gmail.com')
        Freelancer.objects.create(user=user)
        Employer.objects.create(user=user)
        return user

    def createCategory(self):
        category = Category()
        category.category_name = "testCategory" # create category.
        category.save()
        return category
    def createGig(self, user):
        gig = Gig()
        gig.title = 'test_gig'
        gig.description = 'desc'
        gig.country = 'NP'
        gig.city = 'Kathmandu'
        gig.area = 'Hattigauda'
        gig.pay = 100
        gig.user = user
        gig.category = self.createCategory()
        gig.save()
        return gig

    def test_jobdetail_template(self):
        self.user = self.createUser()
        self.gig = self.createGig(self.user)
        response = self.client.get('/gig/jobdetail/'+str(self.gig.id))
        self.assertTemplateUsed(response, 'jobdetail.html')
    
    def test_apply_job(self):
        self.user = self.createUser()
        self.gig = self.createGig(self.user)
        response = self.client.post('/gig/applyjson/', {'user':self.user.id, 'gig': self.gig.id})
        self.assertEqual(response.content, b'6969')
    
    def test_double_apply_job(self):
        self.user = self.createUser()
        self.gig = self.createGig(self.user)
        response1 = self.client.post('/gig/applyjson/', {'user':self.user.id, 'gig': self.gig.id})
        response2 = self.client.post('/gig/applyjson/', {'user':self.user.id, 'gig': self.gig.id})
        self.assertEqual(response2.content, b'69420')