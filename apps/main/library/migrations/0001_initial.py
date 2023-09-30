# Generated by Django 4.2.4 on 2023-09-24 16:27

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Librarys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('year_range', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
