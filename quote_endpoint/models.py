from django.db import models
import requests
import pandas as pd
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&outputsize=full&apikey=K8M3E4D6ZBNJHHHF

class Quote(models.Model):
    symbol = models.CharField(max_length=10)
    open = models.IntegerField(default=0)
    high = models.IntegerField(default=0)
    low = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    volume = models.IntegerField(default=0)
    latest_trading_date = models.DateTimeField('latest trading date')
    previous_close = models.IntegerField(default=0)
    change = models.IntegerField(default=0)
    change_percent = models.IntegerField(default=0)

    def get_quote_data_time_series_daily(symbol):
        url_pre = "https://www.alphavantage.co/query?function="
        url_function_time_series_daily = "TIME_SERIES_DAILY&"
        url_symbol = "symbol="
        url_outputsize = "&outputsize=full"
        url_apikey = "&apikey=K8M3E4D6ZBNJHHHF"
        quote_data = requests.get(url_pre + url_function_time_series_daily + url_symbol + symbol + url_outputsize + url_apikey)
        return quote_data

    def __str__(self):
        return self.symbol

class Day_to_Day_Volatility(models.Model):   # Measuring percentage change from one day to two, one day to three, and so on to five.
    def get_quote_data_time_series_daily(symbol):
        url_pre = "https://www.alphavantage.co/query?function="
        url_function_time_series_daily = "TIME_SERIES_DAILY&"
        url_symbol = "symbol="
        url_outputsize = "&outputsize=full"
        url_apikey = "&apikey=K8M3E4D6ZBNJHHHF"
        quote_data = requests.get(url_pre + url_function_time_series_daily + url_symbol + symbol + url_outputsize + url_apikey)
        return quote_data



    def day_two(symbol):
        equity = get_quote_data_time_series_daily(symbol)
        equity_to_json = equity.json()
        equity_history = equity_to_json[list(equity_to_json.keys())[1]]
        equity_history_df = pd.DataFrame.from_dict(equity_history, orient='index')
        df_close = equity_history_df['4. close'].to_frame()[::-1].astype(float)

        df_close['day_2'] = (df_close['4. close'][1] - df_close['4. close'][0]) / df_close['4. close']
        # the above is not quite there


        # data frame with closing prices
        # iterate over data frame processing percentage change of one, two, three, four, five days percentage change
        # populate seperate data frame with percentage change with columns number of days
        # equity_history = symbol['4. close'] - day before['4. close']

        return day_two_percentage_change
