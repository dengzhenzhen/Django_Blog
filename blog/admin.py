from django.contrib import admin
from .models import *
# Register your models here.
# SuperUser: 
# User name:test
# Password:test123456
admin.site.register(blog_post)
admin.site.register(blog_information)