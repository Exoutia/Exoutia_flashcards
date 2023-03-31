from django.shortcuts import render
from django.views.generic import (ListView,)
from .models import Card

class CardListView(ListView):
    model = Card
    queryset = model.objects.all().order_by("box", "-date_created")