from django.shortcuts import render

from .models import Quote

# import urllib.request
import json
import requests

def index(request):
    API_call_futures = requests.get("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=YM=F&apikey=K8M3E4D6ZBNJHHHF")
    API_call_to_json = API_call_futures.json()
    DJIA_futures = API_call_to_json['Global Quote']
    
    context = {'DJIA_futures': DJIA_futures}
    return render(request, 'quote_endpoint/index.html', context)
