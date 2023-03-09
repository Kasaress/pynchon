from django.contrib import admin

from users.forms import CreationForm
from users.models import User


@admin.action(description='Сделать активными')
def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description='Деактивировать')
def make_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """ Модель для управления пользователями в админке. """

    form = CreationForm
    list_display = ('id', 'first_name', 'last_name', 'email', 'is_active',)
    search_fields = ('first_name', 'last_name', 'email', 'username',)
    search_help_text = 'Поиск по ФИ, почте, нику'
    filter_horizontal = (
        'groups',
        'user_permissions',
    )
    save_on_top = True
    actions = (make_active, make_inactive,)

    fieldsets = (
        ('Общее', {
            'classes': ('wide',),
            'fields': ('is_active', 'last_login', 'date_joined',)
        }),
        ('Данные', {
            'classes': ('wide',),
            'fields': (
                'first_name', 'last_name', 'email',)
        }),
        ('Права', {
            'classes': ('wide',),
            'fields': (
                ('is_staff', 'is_superuser',),)
        }),
        ('Группы', {
            'classes': ('collapse',),
            'fields': (
                ('groups', 'user_permissions',),)
        }),
        ('Пароль', {
            'classes': ('collapse',),
            'fields': (
                ('password1', 'password2',),)
        }),
    )

    add_fieldsets = (
        ('Общее',
         {
             'fields': ('first_name', 'last_name', 'email', 'username',),
         }),
        ('Права',
         {
             'fields': (('is_staff', 'is_superuser',),)
         }),
        ('Пароль',
         {
             'fields': (('password1', 'password2',),)
         }),
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)
