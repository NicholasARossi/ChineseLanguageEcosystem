from django.shortcuts import render
from flashcards import models
from rest_framework import generics, filters



# Create your views here.
class PredictorListCreate(generics.ListCreateAPIView):
    queryset = models.Predictor.objects.all()
    serializer_class = serializers.PredictorSerializer


class PredictorRetrieve(generics.RetrieveAPIView):
    queryset = models.Predictor.objects.all()
    serializer_class = serializers.PredictorSerializer