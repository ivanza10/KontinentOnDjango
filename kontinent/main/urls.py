from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('onas', views.onas),
    path('kontakt', views.kontakt),
    path('grani', views.grani),
    path('chaikovskiy', views.chaikovskiy),
    path('slavniy', views.slavniy)
]