from django.db import models

from django.utils import timezone
 


class Coins(models.Model):
    name  = models.CharField(max_length=128) 
    symbol  = models.CharField(max_length=10)


    class Meta:
        verbose_name_plural = 'Coins'
        #unique combination of fields
        unique_together = (("name", "symbol"),)
    
    def __repr__(self):
        return '<Currency: %r, %r >' % (self.name, self.symbol)

    def __str__(self):
        return '%r, %r ' % (self.name, self.symbol)
 

class Rating(models.Model):

    _db = models.AutoField(primary_key=True)
    rating = models.IntegerField() 
    #name_coin = models.ForeignKey(
    #    'Coins',
    #    on_delete=models.CASCADE,
    #)
    name_coin = models.ForeignKey(Coins, related_name='coin_name',
                               on_delete=models.CASCADE, null=True)
    market_cap = models.DecimalField(max_digits=14, decimal_places=2)
    price = models.DecimalField(max_digits=18, decimal_places=6)
    supply = models.DecimalField(max_digits=18, decimal_places=3)
    volume = models.DecimalField(max_digits=18, decimal_places=3)
    h1 = models.FloatField()
    h24 = models.FloatField()
    d7 = models.FloatField()
    pub_date = models.DateTimeField(default=timezone.now)


    class Meta:
        get_latest_by = 'pub_date'
        ordering = ["-pub_date"]
        
    def __repr__(self):
        return '%r, %r, %r, %r' % (self.rating, self.name_coin.symbol, self.price,  self.pub_date.strftime('%Y-%m-%d %H:%M'))

    def __str__(self):
        return '%r, %r, %r, %r, %r, %r, %r, %r, %r, %r, %r' % (self.rating, self.name_coin.symbol, self.name_coin.name,
                                    self.market_cap, self.price, self.supply, self.volume,
                                   self.h1, self.h24, self.d7,   self.pub_date.strftime('%Y-%m-%d %H:%M'))

