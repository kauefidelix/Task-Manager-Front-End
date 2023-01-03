from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cards/<uuid:card_id>/', views.card_detail, name='card_detail'),
]