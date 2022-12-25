from django.shortcuts import render
from django.http import HttpResponse
from core.models import Card
from datetime import date
# Create your views here.

def index(request):
    cards = Card.objects.all()
    today = date.today()
    return render(request, 'index.html', {'cards': cards, 'today': today})
