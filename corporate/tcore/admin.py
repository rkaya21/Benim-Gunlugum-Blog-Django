from django.contrib import admin
from .models import Contact, About, Service, Slider
from modeltranslation.admin import TranslationAdmin
from .admin_mixins import CommonMedia


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'message')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    last_display = ('title',)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')