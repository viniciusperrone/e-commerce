from django.urls import path
from .views import (
    item_list, 
    checkout,
    product,
    create_product
)

app_name = 'store'

urlpatterns = [
    path('inicio', item_list),
    path('checkout', checkout),
    path('produto/<int:id>', product),
    path('produtos/criar', create_product)
]