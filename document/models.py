from django.db import models
from properties.models import Client, Property
# Create your models here.

class ClientDoc(models.Model):
    file = models.FileField(upload_to='static/documents/')
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.client_id.name}"

class PropertyDoc(models.Model):
    file = models.FileField(upload_to='static/documents/')
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.property_id.address}"

