# Generated by Django 3.2.7 on 2021-09-12 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='logo',
            field=models.ImageField(blank=True, upload_to='experience/', verbose_name='Logo'),
        ),
    ]
