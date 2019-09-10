from django.db import models

# https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=YM=F&apikey=K8M3E4D6ZBNJHHHF

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
    def __str__(self):
        return self.symbol
