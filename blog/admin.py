from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(SummernoteModelAdmin):
    """ Admin view for Blog Posts """
    list_display = ('title', 'created', 'updated')
    search_fields = ('title', 'body')
    list_filter = ('title', 'created')
    summernote_fields = ('body')
