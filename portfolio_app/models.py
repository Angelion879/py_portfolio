from django.db import models
from django.utils.text import slugify

# Create your models here.
class Language(models.Model):
    code = models.CharField(max_length=3, primary_key=True)

    def __str__(self):
        return str(self.code)

class Thumbnail(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="post_img")

    def __str__(self):
        return str(self.name)

class Post(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    thumbnail = models.ForeignKey(Thumbnail, on_delete=models.SET_NULL, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    repo_link = models.CharField(max_length=250,null=True, blank=True)
    active = models.BooleanField(default=False)
    fixed = models.BooleanField(default=False)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        if self.slug is None:
            slug = slugify(self.title)

            has_slug = Post.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.title) + '-' + str(count)
                has_slug = Post.objects.filter(slug=slug).exists()

            self.slug = slug

        super().save(*args, **kwargs)

    @property
    def get_thumbnail_url(self):
        if self.thumbnail and self.thumbnail.image:
            return self.thumbnail.image.url
        
        return 'placeholder.png'
