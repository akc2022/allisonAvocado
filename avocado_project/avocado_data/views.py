from django.shortcuts import render
from datetime import datetime
from .models import Avocado_Price
from .models import City_House_Price

def avocado_data(request):
	price_list = Avocado_Price.objects.all()
	return render(request, 'avocado_data/avocado_price_data.html', {"price_list" : price_list})

def home_data(request):
	price_list = City_House_Price.objects.all()
	return render(request, 'avocado_data/house_price_data.html', {"price_list" : price_list})



# Create your views here.
def home(request):
	name ="Allison"
	now = datetime.now()
	current_year = now.year
	price_list = Avocado_Price.objects.all()
	return render(request, 'avocado_data/home.html',{"name" : name, "current_year" : current_year, "price_list" : price_list})

