from django.http import HttpResponse
from django.shortcuts import render
  
def index(request):
    return render(request, "index.html")
 
def contacts(request):
    return render(request, "contacts.html")

def about(request):
    return render(request, "about.html")

def patients(request):
    return render(request, "about.html")

def doctors(request):
    return render(request, "doctors.html")

def cost(request):
    return render(request, "cost.html")

    