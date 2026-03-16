from django.urls import path
from it_inventory.views import *

"""
URL configuration for the it_inventory application.

Each path maps a URL route to a Django view function that will
handle the HTTP request and return a response.
"""
urlpatterns = [

    path('', home, name='home'),
    path('add-insumo/', add_insumo, name='add_insumo'),
    path('add-user/', add_user, name='add_user'),
    path('add-ws/', add_ws, name='add_ws'),
    path('query/', query_insumo, name='query_insumo'),
]
