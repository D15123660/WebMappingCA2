from django.http import HttpResponse
from django.shortcuts import render

from . import apps


def service_worker(request):
    response = HttpResponse(open(apps.PWA_SERVICE_WORKER_PATH).read(), content_type='application/javascript')
    return response


def manifest(request):
    return render(request, 'manifest.json', {
        setting_name: getattr(apps, setting_name)
        for setting_name in dir(apps)
        if setting_name.startswith('PWA_')
    }, content_type='application/json')


def offline(request):
    return render(request, "offline.html")
