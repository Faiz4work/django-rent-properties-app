from django.db import models

# Create your models here.
class Property(models.Model):
    
    class Meta:
        verbose_name = "property"
        verbose_name_plural = "property"
    address = models.CharField(max_length=200)
    rent = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    rented_since = models.DateField()
    renewal_date = models.DateField()

    total_expenses = models.IntegerField(blank=True, null=True)
    
    rented_to = models.OneToOneField("Client", on_delete=models.SET_NULL, null=True,
                                  blank=True)
    
    def __str__(self):
        return f"{self.address}"
    
    
class Client(models.Model):
    name = models.CharField(max_length=50)
    profile_pic = models.ImageField(blank=True, upload_to='static/images/')
    mobile = models.CharField(blank=True, default='none', max_length=25)
    email = models.CharField(max_length=100, default='none', blank=True)
    documents = models.CharField(max_length=200, default='none', blank=True)
    bank_details = models.CharField(max_length=200, default='none', blank=True)
    history = models.CharField(max_length=200, default='none', blank=True)
    
    def __str__(self):
        return f"{self.name}, {self.email}"
    
    