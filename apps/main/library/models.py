from ckeditor.fields import RichTextField
from django.db import models


class Librarys(models.Model):
    name = models.CharField(max_length=100)
    description = RichTextField(null=True, blank=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    logo = models.ImageField(upload_to='images/', null=True, blank=True)
    year_range = models.CharField(max_length=20)
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.name
