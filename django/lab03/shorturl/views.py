from django.shortcuts import render, redirect
from .models import URL
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.


def short_url(request):
    if request.method == "GET":
        return render(request, 'shorturl/index.html', {})
    if request.method == "POST":
        long_url = request.POST.get('longUrl')
        print(long_url)
        long_url_db = URL.objects.filter(long_url=long_url)
        if long_url_db.count() == 1:
            short_url = {'short_url': long_url_db[0].short_url}
            return JsonResponse(short_url)
        else:
            new_URL = URL.objects.create(long_url=long_url)
            #new_URL.save()
            new_URL.shorten_url(new_URL.pk)
            new_URL.save()
            short_url = {'short_url': new_URL.short_url}
            return JsonResponse(short_url)

# Redirects to short URL.
def url_redirect(request, short_url):
    print(short_url)
    short_url_db = URL.objects.filter(short_url=short_url)
    if short_url_db.count() == 1:
        print(short_url_db[0].long_url)
        return HttpResponseRedirect('http://' + short_url_db[0].long_url)
    else:
        return HttpResponseNotFound()
