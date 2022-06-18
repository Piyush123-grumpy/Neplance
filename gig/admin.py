from django.contrib import admin
from .models import Gig, Category, Application 
# Register your models here.
admin.site.register(Gig)
admin.site.register(Category)
admin.site.register(Application)
