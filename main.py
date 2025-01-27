from whitenoise import WhiteNoise
from biangelis.settings import env
from biangelis.wsgi import application

app = application
app = WhiteNoise(app, root=env("STATIC_HOST"))