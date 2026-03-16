from django.db import models

# Create your models here.
class Insumo(models.Model):
    """
    Model that represents an inventory supply (IT consumable or material).

    Each Insumo stores its name, category and the available quantity.
    """
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    amount = models.IntegerField()

    def __str__(self):
        """
        String representation used in Django admin and debugging.
        """
        return f"{self.category} {self.name}"
class User(models.Model):
    """
    Model representing a user of the IT system.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        """
        Returns the user name as the readable representation.
        """
        return self.name
class WorkStation(models.Model):
    """
    Model representing a workstation or computer registered in the IT inventory.
    """
    ws_number = models.CharField(max_length=200)
    origin = models.CharField(max_length=500)
    state = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    looked_by = models.CharField(max_length=200)
    comments = models.CharField(max_length=500)
    date_received = models.DateField()

    def __str__(self):
        """
        Returns the workstation identifier.
        """
        return self.ws_number