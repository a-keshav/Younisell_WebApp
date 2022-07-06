from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('cowin/', views.cowin, name="cowin"),
	#path('cowin/', RedirectView.as_view(url='https://www.cowin.gov.in/')),
]
