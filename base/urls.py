from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('feed/', views.feed, name="feed"),

    # Language switch path
    path('i18n/', include('django.conf.urls.i18n')),
]
