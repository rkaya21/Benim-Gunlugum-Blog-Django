from django.views.generic import TemplateView, ListView, DetailView
from django.conf import settings
from django.utils import translation
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from urllib.parse import urlparse
from django.http import HttpResponseRedirect
from taggit.models import Tag
from django.db.models import Count
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import get_object_or_404
from tcore.models import Blog, Slider, About, Service, Category


def set_language(request, language):
    try:
        referer_path = urlparse(request.META.get("HTTP_REFERER")).path
        view = resolve(referer_path)
    except Resolver404:
        return HttpResponseRedirect("/")

    translation.activate(language)

    next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)

    return HttpResponseRedirect(next_url)


class BaseView(object):
    """
      View'ler için ortak context sınıfı
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Categories'] = Category.objects.all()  # Tüm kategorileri context'e Ekle
        context['PBlogs'] = Blog.objects.order_by('-views')[:5] # popüler blogları sıralayalım
        context['most_common_tags'] = Tag.objects.annotate(num_times=Count('taggit_taggeditem_items')).order_by('-num_times')[:5]
        return context


class IndexView(ListView):
    """
    Ana Sayfam için oluşturduğum View
    """
    template_name = 'index.html'
    model = Slider

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Sliders'] = Slider.objects.all()  # Tüm Slider verilerini Ekle
        context['Abouts'] = About.objects.first()  # İlk hakkımdamı Ekle
        context['Services'] = Service.objects.all()  # Tüm servis verilerini Ekle
        context['Blogs'] = Blog.objects.all()  # Tüm Blog verilerini Ekle
        return context


class AboutView(ListView):
    """
    Hakkımda Sayfam için oluşturduğum View
    """
    template_name = 'about.html'
    context_object_name = "Abouts"
    queryset = About.objects.first()


class ServiceView(ListView):
    """
    Hizmetler kısmı için oluşturduğum View.
    """
    template_name = 'services.html'
    context_object_name = "Services"
    queryset = Service.objects.all()


class BlogView(BaseView, ListView):  # Not: BaseView önde olmalı.
    """
    Blog listeleri sayfası için oluşturduğum View
    """
    template_name = 'blog.html'
    context_object_name = "Blogs"
    queryset = Blog.objects.all()
    paginate_by = 2


class BlogDetailView(BaseView, DetailView):  # Not: BaseView önde olmalı.
    """
    Blog listesi sayfasında Detaylar butonuna bastığımda açılan detay BlogDetailView
    """
    model = Blog
    template_name = 'blog-details.html'
    context_object_name = "blog"
    slug_url_kwarg = "slug"

    def get_object(self, queryset=None):
        """
        Blog yazımdan herhangi birinde detaylara
        tıklanırsa kaç kere görüntüleneceğini gösteririz.
        """
        obj = super().get_object(queryset=queryset)
        obj.views += 1
        obj.save()
        return obj


class CategoryDetailView(BaseView, ListView):  # Not: BaseView önde olmalı.
    """
    Blog listelerini Dashboard'dan belirli kategoriye göre ekliyorum.Örneğin,
    Felsefe kategorisine bastığınızda Felsefe ile ilgili blogları sorgular.
    """
    model = Blog
    template_name = 'category-details.html'
    context_object_name = "Blogs"

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category, slug=slug)
        return Blog.objects.filter(category=category)


class BlogSearchView(BaseView, ListView):
    model = Blog
    template_name = 'blog-search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Blog.objects.filter(title__icontains=query)
        return Blog.objects.none()


class ContactView(TemplateView):
    template_name = 'contact.html'

    def post(self, request, *args, **kwargs):
        full_name = request.POST.get('fullName')
        phone_number = request.POST.get('phoneNumber')
        email = request.POST.get('email')
        message = request.POST.get('message')

        try:
            send_mail(
                f'{full_name} tarafından yeni bir mesajınız var.',
                f'Mesaj: {message}\nTelefon: {phone_number}\nEmail: {email}',
                'django@recepeneskaya.com.tr',   # Not: örnek
                ['info@recepeneskaya.com.tr'],  # Not: örnek
                fail_silently=False,
            )
            messages.success(request, 'Mesajın başarıyla gönderildi.')
        except Exception as exc:
            messages.error(request, f'Mesaj gönderimi başarısız oldu. {exc}')

        return HttpResponseRedirect(reverse('contact'))
