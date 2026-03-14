from django.urls import path
from it_inventory.views import *

urlpatterns = [
    path('', home, name='index'),
]
