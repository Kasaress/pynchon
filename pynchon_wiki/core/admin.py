from django.contrib import admin

from .models import TopMenu


@admin.register(TopMenu)
class TopMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active', 'name', 'url', 'sort',)
    search_fields = ('name', 'url',)
    readonly_fields = ('created_at',)
