from django.urls import path
from .views import (
    item_list, 
    checkout,
    product,
    create_product,
    about_us
)

app_name = 'store'

urlpatterns = [
    path('inicio', item_list, name='home'),
    path('sobre-nos', about_us, name='about_us'),
    path('checkout', checkout, name='checkout'),
    path('produto/<int:id>', product),
    path('produtos/criar', create_product, name='criar_produtos')
]