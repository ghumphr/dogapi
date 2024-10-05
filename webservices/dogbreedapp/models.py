from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator


# Create your models here.

# adapted from https://mlhale.github.io/CYBR8470/modules/webservices/
class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Breed(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=6, choices=[(a, a) for a in ("Tiny", "Small", "Medium", "Large")])
    friendliness = models.IntegerField(validators=(MaxValueValidator(5), MinValueValidator(1)), choices=[(a, a) for a in range(1, 6)])
    trainability = models.IntegerField(validators=(MaxValueValidator(5), MinValueValidator(1)), choices=[(a, a) for a in range(1, 6)])
    sheddingamount = models.IntegerField(validators=(MaxValueValidator(5), MinValueValidator(1)), choices=[(a, a) for a in range(1, 6)])
    exerciseneeds = models.IntegerField(validators=(MaxValueValidator(5), MinValueValidator(1)), choices=[(a, a) for a in range(1, 6)])

    def __str__(self):
        return self.name







