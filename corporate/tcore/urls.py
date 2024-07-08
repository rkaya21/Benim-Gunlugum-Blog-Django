from django.urls import path
from .views import IndexView, AboutView, ServiceView, BlogView, ContactView, BlogDetailView, CategoryDetailView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about', AboutView.as_view(), name='about'),
    path('services', ServiceView.as_view(), name='services'),
    path('blog', BlogView.as_view(), name='blog'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog-detail'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('contact', ContactView.as_view(), name='contact')
]
