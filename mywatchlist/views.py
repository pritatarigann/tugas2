# import httpresponse
from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    mywatchlist = MyWatchList.objects.all()
    
    watched = MyWatchList.objects.filter(watched=True).count()
    unwatched = MyWatchList.objects.filter(watched=False).count()

    message = ""

    # menampilkan pesan 
    if watched >= unwatched:
        message = "Selamat, kamu sudah banyak menonton!"
    else:
        message = "Wah, kamu masih sedikit menonton!"

    context = {
        "watchlist": mywatchlist,
        "message": message,
        "nama": 'Prita Tarigan',
        "npm": "2106751190"
    }
    return render(request, 'mywatchlist.html', context)

def show_mywatchlist_json(request):
    mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", mywatchlist), content_type="application/json")

def show_mywatchlist_xml(request):
    mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", mywatchlist), content_type="application/xml")

def show_mywatchlist_json_id(request, id):
    mywatchlist = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", mywatchlist), content_type="application/json")

def show_mywatchlist_xml_id(request, id):
    mywatchlist = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", mywatchlist), content_type="application/xml")