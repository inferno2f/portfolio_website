from django.contrib import admin
from .models import Experience

# Register your models here.


class MainAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'period',)


admin.site.register(Experience, MainAdmin)
