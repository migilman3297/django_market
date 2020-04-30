from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Stock


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth import get_user_model


from .forms import StockForm

User = get_user_model()


class Portfolio(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'charts.html')

def get_data(request, *args, **kwargs):

	data = {
	"sales": 100,
	"customers": 10,
	}

	return JsonResponse(data)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
    	import requests
    	import json

    	#if request.method == 'POST':
    	ticker =  "goog"  #equest.POST['ticker']
    	close = []
    	date = []
    	api_request = requests.get("https://sandbox.iexapis.com/stable/stock/twtr/chart/1m?token=Tsk_f2543ab192784b1cba89f8b7b62cdd72")#pk_e9ec00023f724e1ca6a7bcc3fba7d057")
    	#try:
    	api = json.loads(api_request.content)
    	for a in api:
    		close.append(a['close'])
    		date.append(a['date'])

    	data = {
    		"close": close,
    		"date": date
		}
    	#except Exception as e:
    	#	api = "Error..."
    	return Response(data)
#else:
    		#return render(request, 'profile', {'ticker': "Enter a Ticker Above"})
    	

@login_required		
def profile(request):
	return render(request, 'profile.html', {})


def home(request):
	import requests
	import json

	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_e9ec00023f724e1ca6a7bcc3fba7d057")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."
		return render(request, 'home.html', {'api': api})

	else:
		return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})
	
	
def about(request):
	return render(request, 'about.html', {})


def add_stock(request):
	import requests
	import json

	if request.method == 'POST':
		form = StockForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ("Stock Has Been Added"))
			return redirect("add_stock")

	else:	
		ticker = Stock.objects.all()

		output = []
		for tick in ticker:

			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(tick) + "/quote?token=pk_e9ec00023f724e1ca6a7bcc3fba7d057")

			try:
				api = json.loads(api_request.content)
				output.append(api)
			except Exception as e:
				api = "Error..."

		return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})


def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("stock has Been Deleted"))
	return redirect(delete_stock)

	
def delete_stock(request):
	ticker = Stock.objects.all()
	return render(request, 'delete_stock.html', {'ticker':  ticker})
