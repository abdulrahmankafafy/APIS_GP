from django.contrib import admin
from .models import UploadedImage

class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'predict_value']
    list_display_links = ['id']
    search_fields = ['predict_value']

admin.site.register(UploadedImage, UploadedImageAdmin)
