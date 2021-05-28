import base64
import os
import struct
import time

from PIL import Image
from django.http import JsonResponse, HttpResponse
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


def history_api(request):
    filename = r'D:\savetemp\02-20210506-153117-A.tmp'
    tmp = []
    fileopen = open(filename, 'rb')
    size = os.path.getsize(filename)
    for j in range(int(size / 4)):
        data_of_tmp = fileopen.read(4)
        num_of_tmp = struct.unpack('f', data_of_tmp)  ##获得的是元组
        intnum_of_tmp = float(num_of_tmp[0])
        tmp.append(intnum_of_tmp)
    fileopen.close()
    x = 384
    y = 288
    im = Image.new('RGB', (x, y))
    for n in range(0, y):
        for m in range(0, x):
            color = tmp[384 * n + m]
            if color > 300:
                rgb = [255, 0, 0]
            elif color > 270:
                rgb = [255, 165, 0]
            elif color > 240:
                rgb = [255, 215, 0]
            elif color > 210:
                rgb = [255, 255, 0]
            elif color > 180:
                rgb = [173, 255, 47]
            elif color > 150:
                rgb = [0, 255, 0]
            elif color > 120:
                rgb = [0, 255, 255]
            elif color > 90:
                rgb = [0, 191, 255]
            elif color > 60:
                rgb = [30, 144, 255]
            else:
                rgb = [0, 0, 255]
            im.putpixel((m, n), (int(rgb[0]), int(rgb[1]), int(rgb[2])))

    ticks = time.time()
    imgpath = 'D:\\pic\\' + str(ticks) + '.jpg'
    im.save(imgpath)
    im.close()
    bb = base64.b64encode(open(imgpath, 'rb').read())

    return HttpResponse(bb, content_type='image/jpeg')
