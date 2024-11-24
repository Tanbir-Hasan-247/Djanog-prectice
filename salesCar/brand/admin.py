from django.contrib import admin

# Register your models here.
from .models import Brand

class brandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display=['name','slug']

admin.site.register(Brand,brandAdmin)