from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def reddy(request):
  return HttpResponse('<h1><marquee>HI how are you</marquee></h1>')
