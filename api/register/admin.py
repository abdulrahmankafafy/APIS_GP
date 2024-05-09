from django.contrib import admin

from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'account_type', 'phone']
    list_display_links = ['username']
    list_editable = ['account_type']
    search_fields = ['username', 'first_name', 'last_name', 'email', 'account_type', 'phone']
    list_filter = ['account_type']
    exclude = ['confirm_password']

admin.site.register(Person, PersonAdmin)
admin.site.site_header = 'Graduation Project 👨‍💻'
admin.site.site_title = 'Graduation Project'