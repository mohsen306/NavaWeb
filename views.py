from django.shortcuts import render
from django.http import HttpResponse, Http404
#from django.template import loader
from .models import Album
# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums' : all_albums}
    return render(request, 'music/index.html', context)
    '''2)---------------------------------------------------------
    template = loader.get_template('music/index.html')
    context = {
    'all_albums' : all_albums,
    }
    return HttpResponse(template.render(context, request))
    ---------------------------------------------------------------'''
    '''1)---------------------------------------------------------
    html = ''
    all_album = Album.objects.all()
    for album in all_album:
        url = '/music/'+ str(album.id) +''
        html += '<a href="'+ url +'">'+album.album_title+'</a><br/>'
    return HttpResponse(html)
    ---------------------------------------------------------------'''

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("مشنگ این چیه میزنی؟")
    return render(request, 'music/detail.html', {'album': album })
