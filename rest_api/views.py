#import pandas as pd

from django.utils import timezone
from scraper.models import  Rating, Coins
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.db.models import Max
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.db.models import Prefetch

 
from rest_framework import viewsets
from  rest_api.serializers import  CoinSerializer, RatingSerializer




 

class CoinViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Coins.objects.all()
    serializer_class = CoinSerializer

class RatingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    latest = Rating.objects.latest('pub_date')
    queryset = Rating.objects.filter(pub_date = latest.pub_date)

    serializer_class = RatingSerializer

 
