from django.shortcuts import render
from django.http import JsonResponse
from stocks.models import Stock
# Create your views here.

def heatmap(request):
    return render(request, 'heatmap.html')

def stock_data(request):
    stocks = Stock.objects.all()
    data = [{"ticker": s.ticker, "price": s.price, "change": s.change} for s in stocks]
    return JsonResponse(data, safe=False)