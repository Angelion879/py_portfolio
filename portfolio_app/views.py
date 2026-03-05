from django.shortcuts import render, redirect
from django.utils.translation import gettext as _, get_language
from django.contrib.auth.decorators import login_required

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from biangelis.keys import receiver
from .models import Post
from .forms import PostForm

wlpp_repeat = lambda: list(range(1,151))

# Create your views here.
def home(request):
    repeat = lambda: list(range(1, 15))

    context = {'repeat':repeat}
    return render(request, 'pages/home.html', context)

def contact(request):
    context = {'repeat':wlpp_repeat}
    return render(request, 'pages/contact.html', context)

# Email sending feat
def send_email(request):

    if request.method == 'POST':
        template = render_to_string('email_structure.html',{
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message'],
        })

        email = EmailMessage(
            subject=request.POST['subject'],
            body=template,
            from_email=settings.EMAIL_HOST_USER,
            to=receiver
        )

        email.fail_silently=False
        email.send()

    context = {'repeat':wlpp_repeat}
    return render(request, 'pages/confirmation.html', context)

def feed(request):
    user_lang = get_language()
    print(user_lang)
    if str(user_lang) == 'pt':
        posts = Post.objects.filter(language='pt', active=True)
    else:
        posts = Post.objects.filter(language='en', active=True)

    context = {'posts':posts}
    return render(request, 'pages/feed.html', context)

def post(request, slug):
    post_repeat = lambda: list(range(1,500))
    content = Post.objects.get(slug=slug)

    context = {'post':content, 'repeat':post_repeat}
    return render(request, 'pages/post.html', context)

# CRUD views

@login_required(login_url="home")
def create_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('feed')

    context = {'form':form, 'repeat':wlpp_repeat}
    return render(request, 'CRUD/create.html', context)

@login_required(login_url="home")
def update_post(request,slug):
    up_post = Post.objects.get(slug=slug)
    form = PostForm(instance=up_post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=up_post)
        if form.is_valid():
            form.save()
        return redirect('feed')

    context = {'form':form, 'repeat':wlpp_repeat}
    return render(request, 'CRUD/create.html', context)

@login_required(login_url="home")
def delete_post(request,slug):
    del_post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        del_post.delete()
        return redirect('feed')
    context={'item':del_post}
    return render(request, 'CRUD/delete.html', context)
