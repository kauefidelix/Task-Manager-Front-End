from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from TaskFront.core.forms import CardForm
from core.models import Card
from datetime import date
# Create your views here.

def index(request):
    cards = Card.objects.all()
    today = date.today()
    return render(request, 'index.html', {'cards': cards, 'today': today})

def view_card(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('view_card', card_id=card.card_id)
    else:
        form = CardForm(instance=card)
    context = {
        'card': card,
        'form': form,
    }
    return render(request, 'card.html', context)
