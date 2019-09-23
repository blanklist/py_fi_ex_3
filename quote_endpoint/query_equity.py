from django.shortcuts import render
from django.http import HttpResponse
from django import forms

class Form_query_equity(forms.Form):
    equity = forms.CharField(label="Equity", max_length = 6)

def page(request):
    if request.POST:
        form = Form_query_equity(request.POST)
        if form.is_valid():
            equity = form.cleaned_data['equity']
            return HttpResponse("Equity added")
        else:
            return render(request, 'templates/query_equity.html', {'form': form})
    else:
        form = Form_query_equity()
        return render(request, 'templates/query_equity.html', {'form': form})
