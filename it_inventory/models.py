from django.db import models

# Create your models here.
class insumo(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.category} {self.name}"
class user(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name
class work_station(models.Model):
    ws_number = models.CharField(max_length=200)
    origin = models.CharField(max_length=500)
    state = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    looked_by = models.CharField(max_length=200)
    comments = models.CharField(max_length=500)
    date_received = models.DateField()

    def __str__(self):
        return self.ws_number