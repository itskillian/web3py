from django.shortcuts import render

from .utils.web3 import fetch_eth_price

def index(request):
    fetch_eth_price()
    return render(request, 'core/index.html')