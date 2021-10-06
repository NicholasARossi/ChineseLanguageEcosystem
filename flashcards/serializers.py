from rest_framework import serializers
from flashcards import models


class CharCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CharCard
        fields = ('deck', 'created_at', 'chinese_text', 'english_text')

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Deck
        fields = ('name')