from django.db import models

# Create your models here.
class wine(models.Model):
    alcohol = models.FloatField(max_length=55)
    malic_acid = models.FloatField(max_length=55)
    ash = models.FloatField(max_length=55)
    alcalinity_of_ash = models.FloatField(max_length=55)
    magnesium = models.FloatField(max_length=55)
    total_phenols = models.FloatField(max_length=55)
    flavanoids = models.FloatField(max_length=55)
    nonflavanoid_phenols = models.FloatField(max_length=55)
    proanthocyanins = models.FloatField(max_length=55)
    color_intensity = models.FloatField(max_length=55)
    hue = models.FloatField(max_length=55)
    od315_of_diluted_wines = models.FloatField(max_length=55)
    proline = models.FloatField(max_length=55)

