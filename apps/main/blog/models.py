from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone


class BlogCategory(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return str(self.text)


class BlogTag(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return str(self.text)


class Blog(models.Model):
    text = models.CharField(max_length=200)
    slug = models.CharField(max_length=500, blank=True)
    image = models.ImageField()
    content = RichTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField(BlogTag)

    def __str__(self):
        return str(self.text)

    def comment_count(self):
        count = BlogComment.objects.filter(blog_id=self.id).count()
        return count

    def save(self, *args, **kwargs):
        self.slug = slugify(self.text)
        super(Blog, self).save(*args, **kwargs)

class BlogComment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.text)
