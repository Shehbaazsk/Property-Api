from django.db import models

# Create your models here.
class State(models.Model):
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.state

class City(models.Model):
    city = models.CharField(max_length=50)
    state = models.ForeignKey(State,on_delete=models.CASCADE)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'

class Property(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    state = models.ForeignKey(State,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'property'
        verbose_name_plural = 'properties'
        