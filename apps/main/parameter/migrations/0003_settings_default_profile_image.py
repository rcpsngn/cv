# Generated by Django 4.2.4 on 2023-10-28 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parameter', '0002_menu_url_alter_menu_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='default_profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='İmage', verbose_name='Default Profil Resmi'),
        ),
    ]
