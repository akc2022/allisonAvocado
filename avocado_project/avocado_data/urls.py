from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('housingprices', views.home_data, name="housing_prices"),
    path('avocadoprices', views.avocado_data, name="avocado_prices"),
]