from django.shortcuts import render
from .models import *


# Create your views here.
def indexView(request):
    search_song = Dynamic.objects.select_related('song').order_by('-dynamic_plays').all()[:8]
    #
    # # 热门搜索，热门下载
    # search_ranking = search_song[:6]

    return render(request, 'index.html', locals())
