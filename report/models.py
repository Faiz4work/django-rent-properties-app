from django.db import models
from properties.models import Property
# Create your models here.

class Expense(models.Model):
    expense_type = models.CharField(max_length=100, blank=True, null=True)
    expense_date = models.DateField()
    amount = models.IntegerField(blank=True, null=True)

    attached_property = models.ForeignKey(Property, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.expense_type}, {self.amount}"


