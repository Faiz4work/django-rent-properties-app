from dataclasses import fields
from tkinter import Widget
from django.forms import ModelForm, DateInput
from .models import Expense


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'

        widgets = {'expense_date': DateInput(attrs={'type': 'date'})}
        
    