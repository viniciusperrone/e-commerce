from django.urls import path
from .views import item_list, checkout

app_name = 'store'

urlpatterns = [
    path('inicio', item_list),
    path('checkout', checkout)
]