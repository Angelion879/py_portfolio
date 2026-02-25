from django.shortcuts import render
from django.utils.translation import gettext as _

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from biangelis.keys import receiver


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
