from django.contrib import admin

# Register your models here.
from .models import Language, Thumbnail, Post

admin.site.register(Language)
admin.site.register(Thumbnail)
admin.site.register(Post)
