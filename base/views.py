from django.shortcuts import render

from .generator import home_repeat

# Create your views here.
def home_page(request):
    repeat = home_repeat()

    context = {'rep':repeat}
    return render(request, 'pages/home.html', context)