from django.contrib import admin

# Register your models here.
from .models import Language, Post

admin.site.register(Language)
admin.site.register(Post)
