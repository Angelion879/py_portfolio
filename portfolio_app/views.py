from django.shortcuts import render
from django.utils.translation import gettext as _, get_language

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from biangelis.keys import receiver
from .models import Post


# Create your views here.
def home(request):
    repeat = lambda: list(range(1, 15))

    context = {'repeat':repeat}
    return render(request, 'pages/home.html', context)

def contact(request):
    wlpp_repeat = lambda: list(range(1,151))

    context = {'repeat':wlpp_repeat}
    return render(request, 'pages/contact.html', context)

# Email sending feat
def send_email(request):
    wlpp_repeat = lambda: list(range(1,151))

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
