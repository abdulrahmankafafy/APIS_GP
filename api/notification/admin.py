from django.contrib import admin

from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'content', 'quantity']
    list_display_links = ['id']
    search_fields = ['user__username', 'user__first_name', 'content', 'quantity']
    list_filter = ['user']

admin.site.register(Notification, NotificationAdmin)