from django.shortcuts import render

from django.utils.translation import gettext as _

# Create your views here.
def home(request):
    context = None
    return render(request, 'pages/home.html', context)
