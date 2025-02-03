from django.urls import path
from stocks import views

urlpatterns = [
    path('', views.heatmap, name='heatmap'),
    path('stock_data/', views.stock_data, name='stock_data'),
]