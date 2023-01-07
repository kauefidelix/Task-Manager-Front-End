from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.http import JsonResponse
from core.models import Card
from datetime import date
import json
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

def update_card_column(request, card_id, newColumn):
    print("Updating card column")
    # Get the card object from the database
    card = Card.objects.get(card_id=card_id)

    # Update the column field
    card.column = newColumn
    card.save()

    return redirect('index')

def save_card_info(request, card_id):
    # Parse the request body to get the card information
    data = json.loads(request.body)
    name = data['name']
    content = data['content']
    column = data['column']

    # Update the card information in the database
    card = Card.objects.get(card_id=card_id)
    card.name = name
    card.content = content
    card.column = column
    card.save()

    # Return the updated card information
    data = {'name': card.name, 'content': card.content, 'column': card.column}
    return HttpResponse(json.dumps(data), content_type='application/json'), render(request, 'card_detail.html', {'card': card})

