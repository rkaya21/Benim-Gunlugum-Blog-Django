from django.urls import path
from .views import IndexView, About


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about', About.as_view(), name='about'),
]
