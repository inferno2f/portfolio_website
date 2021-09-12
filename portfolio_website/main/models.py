from django.db import models


class Experience(models.Model):
    title = models.CharField(max_length=150, verbose_name='Company title')
    position = models.CharField(max_length=150, verbose_name='Occupation')
    period = models.CharField(
        max_length=50, verbose_name='Period of employement')
    location = models.CharField(
        max_length=100, verbose_name='Company location', blank=True)
    description = models.TextField(verbose_name='Overview of the experience')
    logo = models.ImageField(('Logo'), upload_to='experience/', blank=True)
