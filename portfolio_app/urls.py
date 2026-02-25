from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    # Language path
    path('i18n/', include('django.conf.urls.i18n')),
]
