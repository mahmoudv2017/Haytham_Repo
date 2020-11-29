from django.contrib import admin
from my_app import models
# Register your models here.

admin.site.register(models.products)
admin.site.register(models.acounter)