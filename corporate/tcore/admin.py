from django.contrib import admin
from .models import Contact, About, Service, Slider, Category, Blog, Setting
from modeltranslation.admin import TranslationAdmin
from .admin_mixins import CommonMedia


class BaseAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'message')


@admin.register(About)
class AboutAdmin(TranslationAdmin, BaseAdmin):
    list_display = ('title',)


@admin.register(Service)
class ServiceAdmin(TranslationAdmin, CommonMedia):
    last_display = ('title',)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')


@admin.register(Category)
class CategoryAdmin(TranslationAdmin, CommonMedia):
    list_display = ('name',)


@admin.register(Blog)
class BlogAdmin(TranslationAdmin, CommonMedia):
    list_display = ('title', 'created_at', 'updated_at')


@admin.register(Setting)
class SettingAdmin(TranslationAdmin, CommonMedia, BaseAdmin):
    list_display = ('title',)