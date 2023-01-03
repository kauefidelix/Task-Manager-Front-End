from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from core.models import Card
from datetime import date
# Create your views here.

def index(request):
    cards = Card.objects.all()
    today = date.today()
    return render(request, 'index.html', {'cards': cards, 'today': today})

def card_detail(request, card_id):
    # Query the database to get the card with the specified id
    card = Card.objects.get(card_id=card_id)

    # Render the card_detail.html template with the card information
    return render(request, 'card_detail.html', {'card': card})

