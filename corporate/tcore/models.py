from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    full_name = models.CharField(max_length=100, verbose_name=_("Ad Soyad"))
    phone = models.CharField(max_length=15, verbose_name=_("Telefon Numarası"))
    email = models.EmailField()
    message = models.TextField(verbose_name=_("Mesaj"))


class About(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Başlık"))
    content = RichTextField(verbose_name=_("İçerik"))


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Başlık"))
    content = RichTextField(verbose_name=_("İçerik"))
    slug = models.SlugField(max_length=200, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Başlık"))
    image = models.ImageField(upload_to='sliders', verbose_name=_("Resim"))


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("İsim"))
    slug = models.SlugField(max_length=100, unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Başlık"))
    image = models.ImageField(upload_to='blogs', verbose_name=_("Resim"))
    content = RichTextField(verbose_name=_("İçerik"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Kategori"))
    views = models.IntegerField(default=0)
    slug = models.SlugField(max_length=200, unique=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Setting(models.Model):
    logo_1 = models.ImageField(upload_to='dimg', null=True, blank=True)
    logo_2 = models.ImageField(upload_to='dimg', null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name=_("Başlık"))
    description = models.CharField(max_length=255, verbose_name=_("Açıklama"))
    keywords = models.CharField(max_length=255, verbose_name=_("Kelimeler"))
    phone_fixed = models.CharField(max_length=15, verbose_name=_("Telefon"))
    phone_mobile = models.CharField(max_length=15, verbose_name=_("Telefon Numarası"))
    fax = models.CharField(max_length=15)
    email = models.EmailField()
    city = models.CharField(max_length=50, verbose_name=_("Şehir"))
    district = models.CharField(max_length=50, verbose_name=_("İlçe"))
    address = models.TextField(verbose_name=_("Adres"))
    postal_code = models.CharField(max_length=10, verbose_name=_("Posta Kodu"))
    github_url = models.URLField(max_length=255,verbose_name=_("Github"))
    instagram_url = models.URLField(max_length=255, verbose_name=_("Instagram"))
    linkedin_url = models.URLField(max_length=255, verbose_name=_("LinkedIn"))


