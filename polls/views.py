from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello World</h1>")
    
def meme(request):
    return HttpResponse("<img scr='https://www.meme-arsenal.com/memes/4a8e6d4124c75f8de55e002c067c430e.jpg'>")
 