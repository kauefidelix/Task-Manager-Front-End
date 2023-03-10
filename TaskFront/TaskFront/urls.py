"""TaskFront URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from core import views

urlpatterns = [
    path('', views.index),
    path('first_app/', include('core.urls')),
    path('admin/', admin.site.urls),
    path('cards/<uuid:card_id>/', views.card_detail, name='card_detail'),
    path('cards/<uuid:card_id>/saveCardInfo', views.save_card_info, name='save_card_info'),
    path('cards/<uuid:card_id>/update_column/<str:newColumn>', views.update_card_column, name='update_card_column'),
    path('cards/create', views.create_card, name='create_card'),
    path('cards', views.cards, name='cards'),
    path('cards/<uuid:card_id>/delete', views.delete_card, name='delete_card')
]
