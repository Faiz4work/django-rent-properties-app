from django.shortcuts import render
from .forms import ExpenseForm
from properties.models import Property
from .models import Expense
import datetime
# Create your views here.


# function to add expense to selected property
def add_expense_to_property(form):
    amount = form.cleaned_data['amount']
    property = form.cleaned_data['attached_property']

    # getting selected property
    prop = Property.objects.get(pk=property.pk)
    if prop.total_expenses is None:
        prop.total_expenses = 0
    prop.total_expenses = prop.total_expenses + int(amount)

    prop.save()



def report(request):
    return render(request, "report/report_page.html")

def profit(request):
    properties = Property.objects.all()
    all_profits = []
    for prop in properties:
        exp = prop.total_expenses
        if exp==None:
            exp = 0

        rented_date = prop.rented_since
        now = datetime.datetime.now().date()
        d = now - rented_date
        print(d.days)
        months = int(d.days) / 30
        gross_profit = float(months) * float(prop.rent)
        net_profit = gross_profit - exp
        all_profits.append({
            'Property': prop.address,
            'Net_profit': net_profit,
            'Gross_profit': gross_profit,
            "total_expense": exp,
        })

        context = { "Profit": all_profits }

    return render(request, "report/profit.html", context)

def expenses(request):
    props = Property.objects.all()
    context = {"props": props}
    return render(request, "report/expense.html", context)

def add_expense(request):
    form = ExpenseForm()
    mess = None
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            add_expense_to_property(form)
            form.save()
            mess = "Form Data has been submitted."
            form = ExpenseForm()
    context = {
        "form": form,
        "message": mess,
    }
    return render(request, "report/add_expense_form.html", context)

def expense_details(request, pk):
    prop = Property.objects.get(pk=pk)
    expense_list = Expense.objects.all().filter(attached_property=pk)
    context = {"expense_list": expense_list, "t_expense": prop.total_expenses}
    return render(request, "report/expense_details.html", context)