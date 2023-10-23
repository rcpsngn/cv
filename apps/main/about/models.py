from django.db import models


class Career(models.Model):
    text = models.CharField(max_length=200)
    content = models.TextField()
    start_year = models.CharField(max_length=200)
    finish_year = models.CharField(max_length=200)

    def __str__(self):
        return str(self.text)

class Skills(models.Model):
    text = models.CharField(max_length=200)
    count = models.IntegerField()

    def __str__(self):
        return str(self.text)