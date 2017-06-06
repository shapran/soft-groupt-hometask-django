import pandas as pd

from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from scraper.models import Coins, Rating


@login_required(login_url="/login/")
def statistics(request):     
    ''' Display estimated weekly profit for $100 for currencies with weekly growth in interval 10% and 100%  '''

    df = pd.DataFrame( list( Rating.objects.all().values('rating', 'name_coin',
                                                        'market_cap', 'price', 'supply', 'volume',
                                                        'h1', 'h24', 'd7', 'pub_date')[:830]) )
    df_coins = pd.DataFrame( list( Coins.objects.all().values('coin_name', 'name', 'id', 'symbol')) )

    df = df.merge(df_coins, left_on='name_coin', right_on='coin_name', how='left')
    
    growth = df['d7'].astype(float) 
    df['estimated_profit'] =  100.0 * growth
    df = df[ (df.d7 >= 10) & (df.d7 <= 100) ].sort_values(['d7'], ascending=False)

    return render(request, 'statistic/some.html', {'ratings': df.to_dict(orient='records')} )
    
  
