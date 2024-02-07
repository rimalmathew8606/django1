from django.shortcuts import render
from app.models import Movie

def home(request):
    m=Movie.objects.all()
    return render(request,'home.html',{'m':m})
