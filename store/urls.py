from django.urls import path
from .views import item_list

app_name = 'store'

urlpatterns = [
    path('store', item_list, name='item_list')
]