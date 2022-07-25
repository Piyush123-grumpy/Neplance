
from django.urls import reverse
from django.test import TestCase
from .forms import FreelancerSignUpForm
from account.models import User,Freelancer

class UnitTestCase(TestCase):
    def test_register_page_template(self):
        response=self.client.get(reverse('register'))
        self.assertTemplateUsed(response,'account/register.html')
    
    def test_login_successful(self):
        user=User.objects.create(username='ok',password="9808371691abc",email='piyush.ratna.65@gmail.com')
        user.is_active =True
        user.is_freelancer=True
        user.save()
        response=self.client.post(reverse('logina'),{'username':'ok','password':'9808371691abc'})
        self.assertEqual(response.status_code,302)
        return response

    def test_from(self):
        form=FreelancerSignUpForm(data={
            'username':'Okay',
            'email':'piyush.ratna.66@gmail.com',
            'password1':'9808371691abc',
            'password2':'9808371691abc'
        })
        self.assertTrue(form.is_valid())

    def test_freelancer(self):
        user=User.objects.create(username='ok',password="9808371691abc",email='piyush.ratna.65@gmail.com')
        freelancer=Freelancer.objects.create(user=user,language='english',education='+2',current_job='Software Engineer',city='Ktm')
        gotten_freelancer=Freelancer.objects.get(user='1')
        self.assertEquals(freelancer,gotten_freelancer)
