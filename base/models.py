from django.db import models

from django.utils.text import slugify

# Create your models here.


class Language(models.Model):
    code = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return str(self.code)


class Post(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to="image", default="image/placeholder.png")
    body = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=False)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(null=True, blank=True)

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
