import yfinance as yf 
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.core.management.base import BaseCommand
from .models import Stock

'''
Functions for setup and updating DB content.
'''

# Fetch S&P 500 stock data
def fetch_sp500_data():
    sp500_tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]
    stocks_data = []
    
    for ticker in sp500_tickers:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")
        if not data.empty:
            price = data['Close'].iloc[-1]
            change = ((price - data['Open'].iloc[-1]) / data['Open'].iloc[-1]) * 100
            
            stocks_data.append({
                "ticker": ticker,
                "price": round(price, 2),
                "change": round(change, 2)
            })
            
            # Save to DB
            Stock.objects.update_or_create(
                ticker=ticker,
                defaults={"price": price, "change": change}
            )
    return stocks_data
