# Benim Günlüğüm — Kişisel Blog Projesi

2024 yılında Django öğrenme sürecimde geliştirdiğim kişisel blog uygulaması. Amacım Django'nun MVT yapısını pratikte kavramak ve kendi fikirlerimi paylaşabileceğim dinamik bir web sitesi oluşturmaktı.

## Kullandığım Teknolojiler

- Python / Django
- Bootstrap
- JavaScript
- SQLite

## Özellikler

- Anasayfa, Hakkımda, Hizmetler, Blog ve İletişim sayfaları
- Admin panelden blog yazısı, kategori, slider ve servis yönetimi
- Blog yazılarına etiket (taggit) ve kategori desteği
- Blog arama ve kategoriye göre filtreleme
- Sayfalama (pagination)
- Görüntülenme sayacı (her blog detay ziyaretinde artar)
- İletişim formu — SMTP ile e-posta gönderimi
- Çoklu dil desteği (Django Localization)
- Django Template ile dinamik sayfa yapısı

## Kurulum

```bash
git clone https://github.com/rkaya21/django-my-blog.git
cd django-my-blog/corporate

# Ortam değişkenlerini ayarla
cp .env.example .env
# .env dosyasını düzenle: DJANGO_SECRET_KEY ve e-posta ayarları

# Bağımlılıkları kur
pip install -r requirements.txt

# Veritabanını oluştur
python manage.py migrate

# Sunucuyu başlat
python manage.py runserver
```

## Notlar

- Gizli anahtarlar `.env` dosyasında tutulur, repo'ya eklenmez.
