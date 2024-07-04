from modeltranslation.translator import register, TranslationOptions
from .models import About, Service


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title',)