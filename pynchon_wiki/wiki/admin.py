from django.contrib import admin
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields, widgets

from .models import (Book, Chapter, Comment, TableChronology, ChapterLink,
                     CommentLink, Article, User)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Общее', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('is_active', 'created_at', 'deleted_at',)
        }),
        ('Данные', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('name', 'description',)
        }),
    )


class InlineChapterLink(admin.TabularInline):
    model = ChapterLink
    extra = 2
    fields = ('link', 'chapter', 'is_active',)
    verbose_name = 'Ссылка'
    verbose_name_plural = 'Ссылки'


class ChapterResource(resources.ModelResource):
    book_id = fields.Field(
        column_name='book_id',
        attribute='book',
        widget=widgets.ForeignKeyWidget(Book, 'id')
    )

    class Meta:
        model = Chapter
        exclude = ('image', 'summary', 'interpretation')
        fields = (
            'id',
            'number',
            'description',
            'book_part'
        )


@admin.register(Chapter)
class ChapterAdmin(ImportExportModelAdmin):
    resource_classes = [ChapterResource]
    list_display = (
        'id',
        'number',
        'book',
        'book_part',
        'preview',
        'get_links'
    )
    search_fields = ('number',)
    list_filter = ('number', 'book')
    inlines = (InlineChapterLink,)
    readonly_fields = ('preview', 'created_at',)

    fieldsets = (
        ('Общее', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('is_active', 'created_at', 'deleted_at',)
        }),
        ('Данные', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('number', 'book', 'book_part',)
        }),
        ('Описание', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('description', 'summary', 'interpretation',)
        }),
        ('Изображение', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('image', 'preview',)
        }),
    )

    @staticmethod
    @admin.display(description='Ссылки')
    def get_links(obj):
        """
        Метод выводит список ссылок, которые привязаны к главе.
        """

        return [link for link in obj.chapters.all()]

    @admin.display(description='Превью')
    def preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}"'
                f'style="max-height: 200px; max-width: 200px;">'
            )
        else:
            return 'Нет картинки'


class InlineCommentLink(admin.TabularInline):
    model = CommentLink
    extra = 2
    fields = ('link', 'comment', 'is_active',)
    verbose_name = 'Ссылка'
    verbose_name_plural = 'Ссылки'


class CommentResource(resources.ModelResource):
    book_id = fields.Field(
        column_name='book_id',
        attribute='book',
        widget=widgets.ForeignKeyWidget(Book, 'id')
    )
    chapter_id = fields.Field(
        column_name='chapter_id',
        attribute='chapter',
        widget=widgets.ForeignKeyWidget(Chapter, 'id')
    )
    author_id = fields.Field(
        column_name='author_id',
        attribute='author',
        widget=widgets.ForeignKeyWidget(User, 'id')
    )

    class Meta:
        model = Comment
        exclude = ('created_at', 'is_active', 'deleted_at')
        fields = (
            'id',
            'page_number_by_2012',
            'page_number_by_2021',
            'name',
            'comment_text',
            'image',
            'sort',
        )


@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    resource_classes = [CommentResource]
    list_display = (
        'name', 'comment_text', 'page_number_by_2012', 'sort', 'preview',
        'get_links')
    inlines = (InlineCommentLink,)
    search_fields = ('comment_text',)
    list_filter = ('book', 'chapter', 'page_number_by_2012', 'sort')
    readonly_fields = ('preview', 'created_at',)

    fieldsets = (
        ('Общее', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('is_active', 'created_at', 'deleted_at',)
        }),
        ('Описание', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('name', 'comment_text',)
        }),
        ('Данные по книге', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('author', ('book', 'chapter',), 'page_number_by_2012',
                       'page_number_by_2021', 'sort',),
        }),
        ('Изображение', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('image', 'preview',)
        }),
    )

    @staticmethod
    @admin.display(description='Ссылки')
    def get_links(obj):
        """
        Метод выводит список ссылок, которые привязаны к комментарию.
        """

        return [link for link in obj.comments.all()]

    @admin.display(description='Превью')
    def preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}"'
                f'style="max-height: 200px; max-width: 200px;">'
            )
        else:
            return 'Нет картинки'


class TableChronologyResource(resources.ModelResource):

    class Meta:
        model = TableChronology
        exclude = ('id', 'created_at', 'is_active', 'deleted_at')
        import_id_fields = ('sort', 'date', 'description')


@admin.register(TableChronology)
class TableChronologyAdmin(ImportExportModelAdmin):
    resource_classes = [TableChronologyResource]
    list_display = ('created_at', 'description', 'sort')
    search_fields = ('created_at', 'description', 'sort')
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Общее', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('is_active', 'created_at', 'deleted_at',)
        }),
        ('Описание', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('date', 'sort', 'description',)
        }),
    )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'author', 'image')
    search_fields = ('text',)
