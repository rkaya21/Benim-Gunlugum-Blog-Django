from django.contrib import admin
from .models import Contact, About, Service
from modeltranslation.admin import TranslationAdmin
from .admin_mixins import CommonMedia


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'message')


@admin.register(About)
class AboutAdmin(TranslationAdmin, CommonMedia):
    list_display = ('title',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    last_display = ('title',)
