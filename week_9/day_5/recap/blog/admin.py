from django.contrib import admin
from .models import Blog, Author, Comment

# Register your models here.
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Comment)
