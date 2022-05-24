from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Freelancer)
admin.site.register(Employer)
admin.site.register(employment_history)
admin.site.register(Other_experience)
admin.site.register(portfolio)