from django.views.generic import TemplateView, ListView
from django.conf import settings
from django.utils import translation
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from urllib.parse import urlparse
from django.http import HttpResponseRedirect

from tcore.models import Blog, Slider, About


def set_language(request, language):
    try:
        referer_path = urlparse(request.META.get("HTTP_REFERER")).path
        view = resolve(referer_path)
    except Resolver404:
        return HttpResponseRedirect("/")

    translation.activate(language)

    next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)

    return HttpResponseRedirect(next_url)


class IndexView(ListView):
    template_name = 'index.html'
    model = Slider

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Sliders'] = Slider.objects.all()
        context['Abouts'] = About.objects.first()
        return context


class AboutView(ListView):
    template_name = 'about.html'
    context_object_name = "Abouts"
    queryset = About.objects.first()


class ServiceView(TemplateView):
    template_name = 'services.html'


class BlogView(TemplateView):
    template_name = 'blog.html'
    queryset = Blog.objects.all()


class ContactView(TemplateView):
    template_name = 'contact.html'
