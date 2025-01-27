from django.shortcuts import render

from django.utils.translation import gettext as _, get_language

from .generator import home_repeat

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
