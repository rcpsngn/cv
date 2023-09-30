from ckeditor.fields import RichTextField
from django.db import models

class MainPage(models.Model):
    text = models.CharField(blank=True, max_length=200, verbose_name="Site Başlığı", null=True)
    slayt_text = models.CharField(blank=True, max_length=500, verbose_name="Slayt Yazısı", null=True)
    slayt_content = RichTextField(blank=True, verbose_name="Slayt Metni", null=True)
    slayt_image = models.ImageField(blank=True, max_length=200, verbose_name="Slayt Görsel", null=True, upload_to="image")

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = "Ana Sayfa Ayarları"
        verbose_name_plural = "Ana Sayfa"