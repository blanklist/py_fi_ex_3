from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Quote, Day_to_Day_Volatility, Form_query_equity
from .models import Day_to_Day_Volatility
import json
import requests
import pandas as pd


def index(request):
    API_call = Quote.get_quote_data_time_series_daily("TSLA").json()
    # API_call_to_json = API_call.json()
    ticker_history = API_call['Time Series (Daily)']
    context = {'ticker_history': ticker_history}
    return render(request, 'quote_endpoint/index.html', context)

def pct_change_view(request, equity):
    pct_change = Day_to_Day_Volatility.pct_change(equity)
    pct_change_to_html = pct_change.to_html()
    context = {'pct_change_to_html': pct_change_to_html}
    return render(request, 'quote_endpoint/pct_change_view.html', context)

def query_equity(request):
    if request.POST:
        form = Form_query_equity(request.POST)
        if form.is_valid():
            equity = form.cleaned_data['equity']
            # return HttpResponseRedirect('pct_change_view', {'equity': equity})
            return render(request, 'quote_endpoint/pct_change_view.html', {'equity': equity})
            # return HttpResponse("Equity added")
        else:
            return render(request, 'quote_endpoint/query_equity.html', {'form': form})
    else:
        form = Form_query_equity()
        return render(request, 'quote_endpoint/query_equity.html', {'form': form})
