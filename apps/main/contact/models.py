from django.db import models



class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    tel = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return str(self.name)
