# Generated by Django 3.2.7 on 2021-09-12 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Company title')),
                ('position', models.CharField(max_length=150, verbose_name='Occupation')),
                ('period', models.CharField(max_length=50, verbose_name='Period of employement')),
                ('location', models.CharField(blank=True, max_length=100, verbose_name='Company location')),
                ('description', models.TextField(verbose_name='Overview of the experience')),
            ],
        ),
    ]
