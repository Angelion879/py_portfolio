from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),

    # Send Email Path
    path('send_email/', views.send_email, name='send_email'),

    # Language path
    path('i18n/', include('django.conf.urls.i18n')),
]
