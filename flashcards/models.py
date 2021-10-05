from django.db import models
from core.utils.scrapers import get_example_sentances

# Create your models here.



class Deck(models.Model):
    name = models.CharField(max_length=64, unique=True)




class CharCard(models.Model):
    deck = models.ForeignKey(
        'Deck',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    chinese_text = models.CharField(max_length=10)
    english_text = models.CharField(max_length=64)


    # created_at = models.DateTimeField(auto_now_add=True)
    # input_values = JSONField(default=dict)
    # output_values = JSONField(default=dict, blank=True)
    # cartographer_version = models.CharField(max_length=128, null=True, blank=True)
    # predictor = models.ForeignKey('crispr.Predictor', blank=True, null=True, on_delete=models.CASCADE,
    #                               related_name='predictions')
