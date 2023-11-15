from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def keeravani(request):
    return render(request,'keeravani.html')

def dsp(request):
    return render(request,'dsp.html')

def thaman(request):
    return HttpResponse('<h1>Thaman has composed morethan 100 films</h1>')