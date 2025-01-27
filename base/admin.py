from django.contrib import admin

# Register your models here.

from .models import Post, Language

admin.site.register(Post)
admin.site.register(Language)
