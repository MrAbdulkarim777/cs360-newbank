from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('cards/', views.cards, name='cards'),
    path('cards/<str:card_name>/', views.card_detail, name='card_detail'),
    path('currency/', views.currency_view, name='currency'),
]
