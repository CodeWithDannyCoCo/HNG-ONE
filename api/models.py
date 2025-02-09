from django.db import models

class NumberProperties(models.Model):
    number = models.IntegerField(unique=True)
    is_prime = models.BooleanField()
    is_perfect = models.BooleanField()
    properties = models.CharField(max_length=255) 
    digit_sum = models.IntegerField()
    fun_fact = models.TextField()