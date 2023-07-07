from django.shortcuts import render, HttpResponse
import datetime
# Create your views here.

def home(request):
    fecha=datetime.datetime.now()
    return render(request,"core/home.html",{"fecha_actual":fecha})
def about(request):
    return render(request,"core/about.html")

def contacto(request):    
    return render(request,"core/contacto.html")