from django.shortcuts import render

from .models import Quote

import urllib.request

def index(request):
    DJIA_futures = urllib.request.urlopen("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=YM=F&apikey=K8M3E4D6ZBNJHHHF")
    context = {'DJIA_futures': DJIA_futures}
    return render(request, 'quote_endpoint/index.html', context)
