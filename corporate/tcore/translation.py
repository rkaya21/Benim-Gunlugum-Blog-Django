from modeltranslation.translator import register, TranslationOptions
from .models import About, Service, Category, Blog, Setting


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Setting)
class SettingTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'keywords',)
