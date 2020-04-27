from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"), 
	path('about.html', views.about, name="about"),
	path('add_stock.html', views.add_stock, name="add_stock"),
	path('delete/<stock_id>', views.delete, name="delete"),
	path('delete_stock.html', views.delete_stock, name="delete_stock"),
	path('sign_in.html', views.sign_in, name="sign_in"),
	path('sign_up.html', views.sign_up, name="sign_up"),
]
