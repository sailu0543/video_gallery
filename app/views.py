from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
def display(request):

    Videos=Videoplayer.objects.all()
    d={'Videos':Videos}

    return render(request,'display.html',d)
def insert(request):
    vf=video_form()
    d={'vf':vf}
    if request.method=='POST' and request.FILES:
        VD=video_form(request.POST,request.FILES)
        if VD.is_valid():
                VD.save()


    return render(request,'insert.html',d)
def home(request):
     return render(request,'home.html')