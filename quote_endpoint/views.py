from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    DJIA_futures = "Here is the logic for pulling dow jones futures latest price and volume."
    return HttpResponse(DJIA_futures)

# Create your views here.
