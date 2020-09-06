from django.shortcuts import render
from WaterLevelApp.models import User,Device
from django.http import HttpResponse
# from django.contrib.auth.forms import


# Create your views here.

def index(request):
    context = {}
    return render(request,"WaterLevelApp/index.html", context)


def sensordata(request):
    return render(request,"WaterLevelApp/Sensordata.html")