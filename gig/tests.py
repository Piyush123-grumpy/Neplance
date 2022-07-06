from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from .views import addgigs
from .models import Category, Gig
from account.models import User

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
        return user

    def createCategory(self):
        category = Category()
        category.category_name = "testCategory" # create category.
        category.save()
        return category
    def createGig(self):
        gig = Gig()
        gig.title = 'test_gig'
        gig.description = 'desc'
        gig.country = 'NP'
        gig.city = 'Kathmandu'
        gig.area = 'Hattigauda'
        gig.pay = 100
        gig.user = self.createUser()
        gig.category = self.createCategory()
        gig.save()
        return gig

    def test_jobdetail_template(self):
        gig = self.createGig()
        response = self.client.get('/gig/jobdetail/1')
        self.assertTemplateUsed(response, 'jobdetail.html')