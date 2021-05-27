from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'baoinformation/index.html')


def index_v1(request):
    return render(request, 'baoinformation/index_v1.html')


def history(request):
    return render(request, 'baoinformation/history.html')


def information(request):
    return render(request, 'baoinformation/information.html')


def maintain(request):
    return render(request, 'baoinformation/maintain.html')


def hardware(request):
    return render(request, 'baoinformation/hardware.html')
