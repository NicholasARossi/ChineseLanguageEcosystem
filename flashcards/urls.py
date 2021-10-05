from django.urls import path

from flashcards import views

app_name = 'flashcards'

urlpatterns = [
    path('cards/', views.PredictorListCreate.as_view(), name='card-list-create'),
    path('cards/<int:pk>', views.PredictorRetrieve.as_view(), name='card-retrieve'),
]


# from django.urls import path
#
# from crispr import views
#
# app_name = 'crispr'
#
# urlpatterns = [
#     path('predictors/', views.PredictorListCreate.as_view(), name='predictor-list-create'),
#     path('predictors/<int:pk>', views.PredictorRetrieve.as_view(), name='predictor-retrieve'),
#     path('predictions/', views.PredictionListCreate.as_view(), name='prediction-list-create'),
#     path('predictions/<int:pk>/', views.PredictionRetrieve.as_view(), name='prediction-retrieve'),
# ]
