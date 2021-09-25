from django.urls import path

from crispr import views

app_name = 'flashcards'

urlpatterns = [
    path('cards/', views.PredictorListCreate.as_view(), name='card-list-create'),
    path('cards/<int:pk>', views.PredictorRetrieve.as_view(), name='card-retrieve'),
]
