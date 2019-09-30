from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from .models import Quote, Day_to_Day_Volatility, Form_query_equity, Equity
import json
import requests
import pandas as pd


def index(request):
    API_call = Quote.get_quote_data_time_series_daily("TSLA").json()
    # API_call_to_json = API_call.json()
    ticker_history = API_call['Time Series (Daily)']
    context = {'ticker_history': ticker_history}
    return render(request, 'quote_endpoint/index.html', context)

def pct_change_view(request, equity="TSLA"):
    pct_change = Day_to_Day_Volatility.pct_change(equity)
    pct_change_to_html = pct_change.to_html()
    context = {'pct_change_to_html': pct_change_to_html}
    return render(request, 'quote_endpoint/pct_change_view.html', context)

def detail_query(request):
    if request.POST:
        form = Form_query_equity(request.POST)
        if form.is_valid():
            equity = form.cleaned_data['equity']
            # request.session['equity'] = requiest.POST['equity']
            form.save()
            # return redirect('pct_change_view', {'equity': equity})
        else:
            return render(request, 'quote_endpoint/detail_query.html', {'form': form})
    else:
        form = Form_query_equity()
        return render(request, 'quote_endpoint/detail_query.html', {'form': form})

def equity_detail(request, equity_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quote_endpoint/detail.html', {'quote': quote})

def query_equity(request):
    quote = get_object_or_404(Quote)
    return render(request, 'quote_endpoint/detail.html', {'quote': quote})
