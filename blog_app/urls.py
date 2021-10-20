from django.urls import path
from .views import (index, ListPubs, DeletePub, InsertPubKeys, getPubID)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('index/', index, name='index'),
    path('lista_pub/', ListPubs, name='ListPubs'),
    path('delete_pub/<int:pk>/', DeletePub, name='DeletePub'),
    path('get_pub/', getPubID, name='getPubID'),
    path('insert_pubkey/', InsertPubKeys, name='InsertPubKeys'),
]

urlpatterns = format_suffix_patterns(urlpatterns)