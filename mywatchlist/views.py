from django.shortcuts import render
from mywatchlist.models import MyWatchListItem
from django.http import HttpResponse
from django.core import serializers

data_mywatchlist = MyWatchListItem.objects.all()
def show_mywatchlist(request):
    watched = 0
    unwatched = 0
    output = ""

    for n in data_mywatchlist:
        if (n.watched_movie): watched += 1
        else: unwatched += 1

    if watched > unwatched : output = "Selamat, kamu sudah banyak menonton!"
    else : output = "Wah, kamu masih sedikit menonton!"    

    context = {
    'nama': 'Sayyid Hafidzurrahman Atstsaqofi',
    'npm': 2106651925,
    'output' : output,
    'watched' : watched,
    'unwatched' : unwatched,
    }

    return render(request, "main.html", context)


context = {
    'list_movie': data_mywatchlist,
    'nama': 'Sayyid Hafidzurrahman Atstsaqofi',
    'npm': 2106651925,
}

def show_mywatchlist_html(request):
    return render(request, "mywatchlist.html", context)

def show_mywatchlist_xml(request):
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")
    
def show_mywatchlist_json(request):
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")

#TODO: Create your views here.
