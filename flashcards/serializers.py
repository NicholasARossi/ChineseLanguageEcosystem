from rest_framework import serializers
from flashcards import models


class CharCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Predictor
        fields = ('pk', 'created_at', 'name', 'input_features', 'output_features', 'trained_model_s3_key',
                  'training_data_s3_key', 'module_s3_key')