from django.contrib import admin
from .models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    """
    Admin view for messages sent to ContactUs
    """
    list_display = ('name', 'email', 'subject', 'created')
    search_fields = ('name', 'email', 'subject', 'body')
    list_filter = ('name', 'email')
