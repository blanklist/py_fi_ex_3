from django.shortcuts import render

from .models import Quote

# import urllib.request
import json
import requests

def index(request):
    API_call_futures = Quote.get_quote_data_time_series_daily("TSLA")
    API_call_to_json = API_call_futures.json()
    TSLA_date = API_call_to_json['Time Series (Daily)']
    TSLA_close = API_call_to_json['Time Series (Daily)']

    context = {'TSLA_date': TSLA_date}
    return render(request, 'quote_endpoint/index.html', context)
