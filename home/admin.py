from django.contrib import admin
from .models import WelcomeMessage


@admin.register(WelcomeMessage)
class WelcomeMessageAdmin(admin.ModelAdmin):
    """Admin view for WelcomeMessage"""
    list_display = ('title', 'body')
    search_fields = ('title', 'body')
