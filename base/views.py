from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _, get_language

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from .models import Post
from .forms import PostForm
from .generator import home_repeat, wlpp_repeat

from biangelis.settings import env

# Create your views here.
def home_page(request):
    repeat = home_repeat()

    context = {'repeat':repeat}
    return render(request, 'pages/home.html',context)

def feed(request):
    user_lang = get_language()
    print(user_lang)
    if str(user_lang) == 'en':
        posts = Post.objects.filter(language='en', active=True)
    else:
        posts = Post.objects.filter(language='pt', active=True)

    context = {'posts':posts}
    return render(request, 'pages/feed.html', context)

def post(request, slug):
    content = Post.objects.get(slug=slug)
    repeat = wlpp_repeat()

    context = {'post':content, 'repeat':repeat}
    return render(request, 'pages/post.html', context)

def contact(request):
    repeat = wlpp_repeat()

    context = {'repeat':repeat}
    return render(request, 'pages/contact.html', context)

# CRUD views

@login_required(login_url="home")
def create_post(request):
    form = PostForm()
    repeat = wlpp_repeat()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('feed')

    context = {'form':form, 'repeat':repeat}
    return render(request, 'pages/post_form.html', context)

@login_required(login_url="home")
def update_post(request,slug):
    up_post = Post.objects.get(slug=slug)
    form = PostForm(instance=up_post)
    repeat = wlpp_repeat()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=up_post)
        if form.is_valid():
            form.save()
        return redirect('feed')

    context = {'form':form, 'repeat':repeat}
    return render(request, 'pages/post_form.html', context)

@login_required(login_url="home")
def delete_post(request,slug):
    del_post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        del_post.delete()
        return redirect('feed')
    context={'item':del_post}
    return render(request, 'pages/delete.html', context)

# Email Send config

def send_email(request):
    repeat = wlpp_repeat()

    if request.method == 'POST':
        template = render_to_string('email_template.html',{
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            [env("EMAIL_RECEIVER")]
        )

        email.fail_silently=False
        email.send()

    context = {'repeat':repeat}
    return render(request, 'pages/email_sent.html', context)
