# Generated by Django 4.2.4 on 2023-09-24 12:30

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=200, null=True, verbose_name='Site Başlığı')),
                ('slayt_text', models.CharField(blank=True, max_length=500, null=True, verbose_name='Slayt Yazısı')),
                ('slayt_content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Slayt Metni')),
                ('slayt_image', models.ImageField(blank=True, max_length=200, null=True, upload_to='image', verbose_name='Slayt Görsel')),
            ],
            options={
                'verbose_name': 'Ana Sayfa Ayarları',
                'verbose_name_plural': 'Ana Sayfa',
            },
        ),
    ]