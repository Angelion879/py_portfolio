from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('feed/', views.feed, name="feed"),
    path('post/<slug:slug>/', views.post, name="post"),
    path('contact/', views.contact, name="contact"),

    # Language switch path
    path('i18n/', include('django.conf.urls.i18n')),

    # CRUD paths
    path('create_post/', views.create_post, name="create_post"),
    path('update_post/<slug:slug>/', views.update_post, name="update_post"),
    path('delete_post/<slug:slug>/', views.delete_post, name="delete_post"),

    # Send Email Path
    path('send_email/', views.send_email, name='send_email')
]
