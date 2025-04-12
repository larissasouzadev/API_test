from django.contrib import admin
from setup import models 
from setup.models import Client, Category, Sales
# Register your models here.
admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Sales)
