from django.shortcuts import render

# Create your views here.


def index(request):
    pass
    return render(request, 'baoinformation/index.html')


def history(request):
    pass
    return render(request, 'baoinformation/history.html')


def information(request):
    pass
    return render(request, 'baoinformation/information.html')


def maintain(request):
    pass
    return render(request, 'baoinformation/maintain.html')


def hardware(request):
    pass
    return render(request, 'baoinformation/hardware.html')
