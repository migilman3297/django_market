from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import Portfolio, get_data, ChartData


urlpatterns = [
	path('profile/', Portfolio.as_view(), name='profile'),
	path('api/data', get_data, name='api-data'),
	path('api/chart/data', ChartData.as_view(), name='api-data'),

	path('', views.home, name="home"), 
	#path('profile/', views.profile, name='profile'),
	 path('about.html', views.about, name="about"),
	path('add_stock.html', views.add_stock, name="add_stock"),
	path('delete/<stock_id>', views.delete, name="delete"),
	path('delete_stock.html', views.delete_stock, name="delete_stock"),

]

urlpatterns += staticfiles_urlpatterns()