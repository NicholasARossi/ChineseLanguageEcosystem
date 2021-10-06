from django.shortcuts import render
from flashcards import models,serializers
from rest_framework import generics, filters



# Create your views here.
class CharCardCreate(generics.ListCreateAPIView):
    queryset = models.CharCard.objects.all()
    serializer_class = serializers.CharCardSerializer


class DeckCreate(generics.ListCreateAPIView):
    queryset = models.Deck.objects.all()
    serializer_class = serializers.DeckSerializer