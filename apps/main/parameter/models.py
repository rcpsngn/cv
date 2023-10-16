from django.db import models

class Settings(models.Model):
    text = models.CharField(blank=True, max_length=200, verbose_name="Site Başlığı", null=True)
    logo = models.ImageField(upload_to="İmage", null=True, blank=True, verbose_name='logo')

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = "Site Ayarları"
        verbose_name_plural = "Site Ayarları"


class Menu(models.Model):
    text = models.CharField(blank=True, max_length=200, verbose_name="Menü Başlığı", null=True)
    url = models.CharField(blank=True, max_length=200, verbose_name="Url", null=True)
    alignment = models.IntegerField(null=True, blank=True, verbose_name="Sıralama")

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = "Menüler"
        verbose_name_plural = "Menüler"