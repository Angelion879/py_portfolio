from django.shortcuts import render

from django.utils.translation import gettext as _, get_language

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from biangelis.settings import env
from .generator import home_repeat, wlpp_repeat
from .models import Post

# Create your views here.
def home_page(request):
    repeat = home_repeat()

    context = {'rep':repeat}
    return render(request, 'pages/home.html', context)

def feed(request):
    user_lang = get_language()
    if str(user_lang) == 'en':
        posts = Post.objects.filter(language='en', active=True)
    else:
        posts = Post.objects.filter(language='pt', active=True)

    context = {'posts':posts}
    return render(request, 'pages/feed.html', context)

def contact(request):
    repeat = wlpp_repeat()

    context = {'repeat':repeat}
    return render(request, 'pages/contact.html', context)

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
            [env('EMAIL_RECEIVER')]
        )

        email.fail_silently=False
        email.send()

    context = {'repeat':repeat}
    return render(request, 'pages/email_sent.html', context)
