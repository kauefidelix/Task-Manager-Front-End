from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.http import JsonResponse
from core.models import Card
from datetime import date
import json
import datetime

def index(request):
    cards = Card.objects.all()
    today = date.today()
    return render(request, 'index.html', {'cards': cards, 'today': today})

def card_detail(request, card_id):
    card = Card.objects.get(card_id=card_id)

    return render(request, 'card_detail.html', {'card': card})

def update_card_column(request, card_id, newColumn):
    print("Updating card column")
    card = Card.objects.get(card_id=card_id)
    card.column = newColumn
    card.save()

    return JsonResponse({'column': card.column})

def save_card_info(request, card_id):
    data = json.loads(request.body)
    name = data['name']
    content = data['content']
    column = data['column']
    card = Card.objects.get(card_id=card_id)
    card.name = name
    card.content = content
    card.column = column
    card.save()
    return JsonResponse({'name': card.name, 'content': card.content, 'column': card.column})

def create_card(request):
    cards = Card.objects.all()
    today = date.today()
    if request.method == 'POST':
        data = json.loads(request.body)
        card = Card.objects.create(
            name=data['name'],
            column=data['column'],
            creation_date = datetime.datetime.strptime(data['creation_date'], '%Y-%m-%d').date(),
            last_modified = datetime.datetime.strptime(data['last_modified'], '%Y-%m-%d').date(),
        )
        return render(request, 'index.html', {'cards': cards, 'today': today})
    return render(request, 'index.html', {'cards': cards, 'today': today})

def cards(request):
    cards = Card.objects.all()
    return JsonResponse(cards, safe=False)


