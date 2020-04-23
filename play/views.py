from django.shortcuts import render

# Create your views here.
def playView(request, page):
    return render(request, 'play.html', locals())
