from django.shortcuts import render

from django.utils.translation import gettext as _

# Create your views here.
def home(request):
    repeat = lambda: list(range(1, 15))

    context = {'repeat':repeat}
    return render(request, 'pages/home.html', context)

def contact(request):
    repeat = lambda: list(range(1,151))

    context = {'repeat':repeat}
    return render(request, 'pages/contact.html', context)

# Email sending feat
