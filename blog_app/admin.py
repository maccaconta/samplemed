
from django.contrib import admin

from .models import Blog, Keywords


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'subtitle',
                    'type',
                    'content',
                    'status',
                    'created_at',
                    'updated_at')


@admin.register(Keywords)
class KeywordsAdmin(admin.ModelAdmin):
    list_display = ('id_pub',
                    'keyword',
                    'created_at',
                    'updated_at')
