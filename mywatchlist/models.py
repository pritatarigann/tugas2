from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class MyWatchList(models.Model):
    watched = models.BooleanField() 
    title = models.CharField(max_length=255)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    release_date = models.DateField()
    review = models.TextField()
