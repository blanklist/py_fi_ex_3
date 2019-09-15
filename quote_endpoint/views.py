from django.shortcuts import render
from .models import Quote
import json
import requests
import pandas as pd

def index(request):
    API_call = Quote.get_quote_data_time_series_daily("TSLA").json()
    # API_call_to_json = API_call.json()
    ticker_history = API_call['Time Series (Daily)']
    context = {'ticker_history': ticker_history}
    return render(request, 'quote_endpoint/index.html', context)

def graph(request):
    API_call = Quote.get_quote_data_time_series_daily("AAPL").json()
    history = API_call['Time Series (Daily)']
    df = pd.DataFrame.from_dict(history, orient='index')
    df_to_json = df.to_json(orient='index')

    context = {'df_to_json': df_to_json}
    # context = {'df': df}
    return render(request, 'quote_endpoint/graph.html', context)
