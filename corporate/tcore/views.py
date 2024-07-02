from django.views.generic import TemplateView
from django.conf import settings
from django.utils import translation
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from urllib.parse import urlparse
from django.http import HttpResponseRedirect


def set_language(request, language):
    try:
        referer_path = urlparse(request.META.get("HTTP_REFERER")).path
        view = resolve(referer_path)
    except Resolver404:
        return HttpResponseRedirect("/")

    translation.activate(language)

    next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)

    return HttpResponseRedirect(next_url)


class IndexView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ServiceView(TemplateView):
    template_name = 'services.html'


class BlogView(TemplateView):
    template_name = 'blog.html'


class ContactView(TemplateView):
    template_name = 'contact.html'
