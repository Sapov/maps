from django.contrib import admin

# Register your models here.
from .models import InfoObjects, Category

admin.site.register(InfoObjects)
admin.site.register(Category)

