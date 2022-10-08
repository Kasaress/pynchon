from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import Book, Chapter, Comment


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'description') 
    search_fields = ('name',) 


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('number', 'book') 
    search_fields = ('number',) 
    list_filter = ('number', 'book') 
    

class CommentAdmin(admin.ModelAdmin):
    def preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')
        else:
            return 'Нет картинки'
    list_display = (
        'origin_text', 'comment_text',
        'page_number_by_2012', 'order_number',
        'preview') 
    search_fields = ('number',) 
    list_filter = ('book', 'chapter', 'page_number_by_2012', 'order_number') 
    readonly_fields = ['preview']

    
    
    
admin.site.register(Book, BookAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Comment, CommentAdmin)
