from ckeditor.fields import RichTextField
from django.db import models

from apps.main.about.models import Skills


class Counter(models.Model):
    text = models.CharField(blank=True, max_length=200, verbose_name="Başlık", null=True)
    count = models.IntegerField()
    oid = models.CharField(max_length=250)

class MainPage(models.Model):
    text = models.CharField(blank=True, max_length=200, verbose_name="Site Başlığı", null=True)
    slayt_text = models.CharField(blank=True, max_length=500, verbose_name="Slayt Yazısı", null=True)
    slayt_skill = models.ManyToManyField(Skills)
    slayt_content = RichTextField(blank=True, verbose_name="Slayt Metni", null=True)
    slayt_image = models.ImageField(blank=True, max_length=200, verbose_name="Slayt Görsel", null=True, upload_to="image")

    contact_text = models.CharField(max_length=250)
    contact_content = RichTextField(blank=True, verbose_name="İletişim Metni", null=True)
    contact_counter = models.ManyToManyField(Counter)
    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = "Ana Sayfa Ayarları"
        verbose_name_plural = "Ana Sayfa"